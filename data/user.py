
from cmath import inf
from config import *
from connect import *



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
    username = str(username)
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
    if(is_password_appropriate(password, min_length=MIN_PASSWORD_LENGTH, max_length=MAX_PASSWOWRD_LENGTH) == False):
        return -5
    

    # Create the connection.
    credentials = read_credentials_from_file("../" + CONNECTION_CREDENTIAL_PATH)
    connection = init_connection(credentials[0], credentials[1], credentials[2], DATABASE_NAME)
    crsr = connection.cursor()

    # See if there is already a user with this username
    sql_command = f"\
        SELECT COUNT(*) FROM {USER_TABLE_NAME}\
        WHERE username = '{username}';\
        "
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

    crsr.close()
    connection.close()

    return ret_code