
from config import connection_credential_path
from connect import *

# Set up the connection and initialize database and
# tables. If database and/or tables are already there,
# skip creating them.
if __name__ == "__main__":

    # Read credential file and create connection
    credentials = read_credentials_from_file("../" + connection_credential_path)
    connection = init_connection(credentials[0], credentials[1], credentials[2])
    