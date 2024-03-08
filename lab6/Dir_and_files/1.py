import os

path = input("Enter a path: ")

if os.path.exists(path):
    directories = []
    files = []

    items = os.listdir(path)

    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)

    print("Directories in the path:", directories)
    print("Files in the path:", files)
    print("All items in the path:", items)
else:
    print("The specified path does not exist.")
