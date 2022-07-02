
from config import *
from connect import *

# Set up the connection and initialize database and
# tables. If database and/or tables are already there,
# skip creating them.
if __name__ == "__main__":

    # Read credential file and create connection.
    credentials = read_credentials_from_file("../" + CONNECTION_CREDENTIAL_PATH)
    connection = init_connection(credentials[0], credentials[1], credentials[2])
    crsr = connection.cursor()

    # If the database doesn't exist, create it.
    sql_command = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};"
    crsr.execute(sql_command)

    # Close the connection.
    crsr.close()
    connection.close()

    # Restart the connection with database as selected database (e.g., social_app).
    credentials = read_credentials_from_file("../" + CONNECTION_CREDENTIAL_PATH)
    connection = init_connection(credentials[0], credentials[1], credentials[2], DATABASE_NAME)
    crsr = connection.cursor()

    # Create user table doesn't exist, create it.
    # Note: max password length is multiplied by 4 since it will be stored in ascii.
    sql_command = f"\
        CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME} (\
            username VARCHAR({MAX_USERNAME_LENGTH}) NOT NULL,\
            first VARCHAR({MAX_FIRST_NAME_LENGTH}),\
            last VARCHAR({MAX_LAST_NAME_LENGTH}),\
            password VARCHAR({MAX_PASSWOWRD_LENGTH * 4}),\
            PRIMARY KEY (username)\
        );"
    crsr.execute(sql_command)

    crsr.close()
    connection.close()
