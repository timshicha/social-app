
from config import connection_credential_path
from connect import *

# Set up the connection and initialize database and
# tables. If database and/or tables are already there,
# skip creating them.
if __name__ == "__main__":

    # Read credential file and create connection.
    credentials = read_credentials_from_file("../" + connection_credential_path)
    connection = init_connection(credentials[0], credentials[1], credentials[2])
    crsr = connection.cursor()
    
    # If the database doesn't exist, create it.
    sql_command = "CREATE DATABASE IF NOT EXISTS social_app;"
    crsr.execute(sql_command)

    # Close the connection.
    crsr.close()
    connection.close()

    # Restart the connection with database as selected database (e.g., social_app).
    credentials = read_credentials_from_file("../" + connection_credential_path)
    connection = init_connection(credentials[0], credentials[1], credentials[2], "social_app")
    crsr = connection.cursor()

    # Create user table doesn't exist, create it.
    sql_command = "\
        CREATE TABLE IF NOT EXISTS social_app (\
            username VARCHAR(50) NOT NULL,\
            first VARCHAR(50),\
            last VARCHAR(50),\
            PRIMARY KEY (username)\
        );"
    crsr.execute(sql_command)

    crsr.close()
    connection.close()
    