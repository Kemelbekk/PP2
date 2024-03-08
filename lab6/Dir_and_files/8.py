import os

def delete(files):
    if os.path.exists(files):
        os.remove(files)
        print(f"the file {files} was deleted")
    else:
        print(f"file {files} was not found")

x = str(input())
delete(x)
