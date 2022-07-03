
# Specify where certain things are (e.g., where the files
# with credentials are stored).
#
# All paths need to be specified from the root directory of
# the web app.
# (i.e., the directory holding the main index.html file).
#
# May be specific to each user.

# For functions that return error codes, a return code of 25
# means success.
SUCCESS_CODE = 25

# Path to file with connection credentials.
# User for creating and managing databases.
CONNECTION_CREDENTIAL_PATH = "../user_credentials.txt"

# Name of this social-app web app database
DATABASE_NAME = "social_app"

# Name of the database table holding the users (along with name, password, etc)
USER_TABLE_NAME = "user"
# Min and max length of username, name, etc.
MIN_USERNAME_LENGTH = 1
MAX_USERNAME_LENGTH = 50
MIN_FIRST_NAME_LENGTH = 1
MAX_FIRST_NAME_LENGTH = 50
MIN_LAST_NAME_LENGTH = 0
MAX_LAST_NAME_LENGTH = 50
MIN_PASSWORD_LENGTH = 4
MAX_PASSWOWRD_LENGTH = 50