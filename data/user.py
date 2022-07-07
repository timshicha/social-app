
import sys
from cmath import inf
from config import *
from connect import *
from parsing_tools import ascii_string_to_string as to_str

NO_FUNCTION_SPECIFIED_ERROR = 1
FUNCTION_DOESNT_EXIST_ERROR = 2
WRONG_NUMBER_OF_ARGS_ERROR = 3

# What gets printed:
# SUCCESS_CODE (see config file) => command ran successfully
# 1 => no function specified (no cmd args)
# 2 => function that was specific doesn't exist
# 3 => function found, but wrong number of args provided
# a negative number => function specific error (please read function error codes).


# See whether the passed username is valid (can be created).
# Requires string to be a string (str).
def validate_string(string, min_length = 0, max_length = inf, extra_legal_chars = None):

    # Null
    if(string == None):
        return False

    # String is too short or too long
    if(len(string) < min_length or len(string) > max_length):
        return False


    # String may only contain alphanumerals and any specified extra characters
    for i in string:
        if(not(str.isalnum(i) or i in extra_legal_chars)):
            return False

    return True

# See whether the passed password is valid (can be created).
# Allows all characters, so only requirement is length.
# Requires password to be a string (str).
def is_password_appropriate(password, min_length = 0, max_length = inf):

    # Null
    if(password == None):
        return False

    # String is too short or too long
    if(len(password) < min_length or len(password) > max_length):
        return False

    return True


# Add a user to the database
#
# Return codes:
# 0  => no error (user was added)
# -1 => username exists
# -2 => database error (connecting, accessing table, etc)
# -3 => username is not appropriate
# -4 => first or last name illegal
# -5 => password illegal
def add_user(username, first_name, last_name, password):

    # Convert to strings for security (and avoid crashes).
    username = str(username).lower() # Usernames will have no capital letters
    first_name = str(first_name)
    last_name = str(last_name)
    password = str(password)

    # Make sure the user entered an appropriate username
    if(validate_string(username, min_length=MIN_USERNAME_LENGTH, max_length=MAX_USERNAME_LENGTH, extra_legal_chars='_') == False):
        return -3

    # Make sure the user enetered an appropriate first and last name
    if(validate_string(first_name, min_length=MIN_FIRST_NAME_LENGTH, max_length=MAX_FIRST_NAME_LENGTH, extra_legal_chars='-') == False or
        validate_string(last_name, min_length=MIN_LAST_NAME_LENGTH, max_length=MAX_LAST_NAME_LENGTH, extra_legal_chars='-') == False):
        return -4

    # Make sure the user entered an appropriate password
    if(is_password_appropriate(password, min_length=(MIN_PASSWORD_LENGTH * 3), max_length=(MAX_PASSWOWRD_LENGTH * 3)) == False):
        return -5
    

    # Create the connection.
    credentials = read_credentials_from_file("../" + CONNECTION_CREDENTIAL_PATH)
    connection = init_connection(credentials[0], credentials[1], credentials[2], DATABASE_NAME)
    crsr = connection.cursor()

    # See if there is already a user with this username
    sql_command = f"\
        SELECT COUNT(*) FROM {USER_TABLE_NAME}\
        WHERE username = '{username}';"

    crsr.execute(sql_command)
    res = crsr.fetchone()

    ret_code = 0

    # If we weren't able to get a result
    if(res == None or len(res) == 0):
        ret_code = -2

    # If there's already a user with the same username
    elif(int(res[0]) > 0):
        ret_code = -1

    # If query ran and the username is unique, add the user
    else:

        sql_command = f"INSERT INTO {USER_TABLE_NAME}\
            VALUES ('{username}','{first_name}','{last_name}','{password}');"
        crsr.execute(sql_command)
        connection.commit()
        ret_code = SUCCESS_CODE

    crsr.close()
    connection.close()

    return ret_code


# Validate user login.
#
# Takes a username and ascii-encoded password.
# Returns true if login successful, false if failed.
#
# Return codes
# 0 => no error (successful login)
# -1 => username doesn't exist
# -2 => username exists but doesn't match the username
def login_user(username, password):

    username = str(username).lower() # Usernames will have no capital letters
    password = str(password)

    # If there are bad characters in the username, the SQL queries may break. So, if
    # bad characters are detected, return a non-existent username right away.
    if(validate_string(username) == False):
        # Non-existent username error
        return -1

    # Create the connection.
    credentials = read_credentials_from_file("../" + CONNECTION_CREDENTIAL_PATH)
    connection = init_connection(credentials[0], credentials[1], credentials[2], DATABASE_NAME)
    crsr = connection.cursor()

    # See if there is a user with this username in the database.
    sql_command = f"\
        SELECT COUNT(*) FROM {USER_TABLE_NAME}\
        WHERE username = '{username}';"

    crsr.execute(sql_command)
    res = int(crsr.fetchone()[0]) # 'res' holds the value of COUNT(*) from SQL

    # Assume no user with this username
    ret_code = -1

    # If there is a user with this username
    if(res != 0):
        sql_command = f"\
            SELECT COUNT(*) FROM {USER_TABLE_NAME}\
            WHERE username = '{username}' AND password = '{password}';"
        
        crsr.execute(sql_command)
        res = int(crsr.fetchone()[0])

        # If the password didn't match with the username...
        if(res == 0):
            ret_code = -2
        # Otherwise the username exists in database and password matches,
        # so return success.
        else:
            ret_code = SUCCESS_CODE
    
    crsr.close()
    connection.close()
        
    return ret_code



# What gets printed:
# 0 => command ran successfully
# 1 => no function specified (no cmd args)
# 2 => function that was specific doesn't exist
# 3 => function found, but wrong number of args provided
# a negative number => function specific error (please read function error codes).
ret_code = NO_FUNCTION_SPECIFIED_ERROR
if __name__ == "__main__":

    # Require an argument (i.e., specify which function to call)
    if(len(sys.argv) < 2):
        ret_code = NO_FUNCTION_SPECIFIED_ERROR
    
    # If a function was specified...
    else:
        # Retrieve the function to call
        func = str(sys.argv[1])

        # Add a user to the database.
        if(func == 'add_user'):
            # Require 4 more args
            if(len(sys.argv) != 6):
                ret_code = WRONG_NUMBER_OF_ARGS_ERROR
            
            # Otherwise add the user.
            # Note: to_str() converts string of ascii values into a proper string (see parsing_tools.py).
            # Note: password will stay as an ascii string so it's properly stores into SQL.
            else:
                ret_code = add_user(to_str(sys.argv[2]), to_str(sys.argv[3]), to_str(sys.argv[4]), sys.argv[5])

        # Validate a user in the database (username and password).
        elif(func == 'login_user'):
            # Require 2 more args
            if(len(sys.argv) != 4):
                ret_code = WRONG_NUMBER_OF_ARGS_ERROR

            # Otherwise attempt to log the user in.
            else:
                ret_code = login_user(to_str(sys.argv[2]), sys.argv[3])

        # If function wasn't found
        else:
            ret_code = FUNCTION_DOESNT_EXIST_ERROR
    

    # What do do with return code:
    print(ret_code) # Just print it