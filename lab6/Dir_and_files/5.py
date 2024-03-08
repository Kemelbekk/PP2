import os
mylist = input("write list element by space: ").split()
data = ' '.join(mylist)
with open("New.txt", 'w') as f:
    f.write(data)

