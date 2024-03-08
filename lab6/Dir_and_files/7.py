#Write a Python program to copy the contents of a file to another file
import os

def toanother(ffile,sfile):
    if os.path.exists(ffile):
        with open(ffile,'r') as fdir:
            with open(sfile, 'w') as sdir:
                sdir.write(fdir.read())
    else:
        print("The read file does not exist")
x = str(input("Provide file that will be copied"))
y = str(input("Write a name for new file"))
toanother(x,y)