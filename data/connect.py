
import mysql.connector

# Create a connection to the database
def init_connection(a_host, a_user, a_password, a_database = None):
    return mysql.connector.connect(
        host = a_host,
        user = a_user,
        password = a_password,
        database = a_database
    )

# Read credentials from user credential file
#
# First line => host
# Second line => user
# Third line => password
def read_credentials_from_file(path):
    credentials = ["","",""]
    
    with open(path) as reader:
        credentials = reader.readlines()
    
    return credentials