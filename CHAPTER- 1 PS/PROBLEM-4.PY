import os

# List all files and directories in the current directory
contents = os.listdir()
print(contents)

# ANOTHER : 


# Specify the path of the directory
path = '/'

# List all files and directories in the specified directory
contents = os.listdir(path)
print(contents)
