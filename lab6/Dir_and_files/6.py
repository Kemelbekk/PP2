import os

for x in range(ord('A'), ord('Z')+1):
    name = chr(x) + '.txt'
    with open(name, 'w') as f:
        f.write(f"content of the file '{name}'")
        