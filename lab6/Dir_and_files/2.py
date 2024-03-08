#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
x = str(input())
if os.path.exists(x):
    if os.access(x, os.F_OK):
        print("Exists")
    else:
        print("Does not exist")
    if os.access(x , os.R_OK):
        print("Readable")
    else:
        print("Does not readable")
    if os.access(x, os.W_OK):
        print("Writeable")
    else:
        print("Does not writable")
    if os.access(x, os.X_OK):
        print("Executable")
    else:
        print("Does not executable")
else:
    print("Does not exist")