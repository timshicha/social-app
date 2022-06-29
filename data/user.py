
from connect import *
from config import connection_credential_path

# Add a user to the database
def add_user(username, first_name, last_name, password):
    
    # Create the connection.
    credentials = read_credentials_from_file("../" + connection_credential_path)
    connection = init_connection(credentials[0], credentials[1], credentials[2], "social_app")
    crsr = connection.cursor()

    # See if there is already a user with this username
    sql_command = f"\
        SELECT COUNT(*) FROM user\
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

        sql_command = f"INSERT INTO user\
            VALUES ('{username}','{first_name}','{last_name}','{password}');"
        crsr.execute(sql_command)
        connection.commit()

    crsr.close()
    connection.close()