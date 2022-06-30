

# Reads a string of ascii values separated by dashes and returns
# a string.
#
# Example: "107-108-109" => "klm"
# Purpose: Passing user-inputed strings as command line arguments may
# create an issue, such as if the user enters characters (like ' '). A
# program using command line arguments would convert the string to an ascii
# string to guarantee that the callee program handles the command line
# arguments as the caller intended.
def ascii_string_to_string(ascii_string):

    if(ascii_string == None):
        return ""

    # Get a list of ascii values
    ascii_string = ascii_string.split('-')

    # Store result into a string
    string = ""

    # Go through each ascii value and convert to char
    for i in ascii_string:

        # Convert each ascii to a char and append to string
        string += chr(int(i))

    return string
