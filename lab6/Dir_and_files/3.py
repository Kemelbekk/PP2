import os

x = str(input())
if os.path.exists(x):
    direc, files = os.path.split(x)
    print("Directory :", direc)
    print("Filename :", files)
else:
    print("Path does not exist")
