import re
pattern = re.compile("a.*b")
x = str(input())
da = pattern.search(x)
if da:
    print("The first occurence was found in index ", da.start())
else:
    print("Was not found")