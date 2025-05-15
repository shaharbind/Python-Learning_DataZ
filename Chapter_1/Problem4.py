'''Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that.'''

import os

# Select the directory path you want to list the content 
directory_path = '/Codez'

try:
    # Retrieve the list of entries in the directory
    entries = os.listdir(directory_path)
    
    # Iterate and print each entry
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
