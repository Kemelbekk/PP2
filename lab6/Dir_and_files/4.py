import os
def cnt(ffile):
    if not os.path.exists(ffile):
        print("Does not exists")
    else:
        with open(ffile, 'r') as f:
            lines = 0
            for line in f:
                lines += 1
            print(f"the number of lines is  + {lines}")

fail = input()
cnt(fail)