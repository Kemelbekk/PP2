import re
pattern = re.compile('ab*')
x = str(input())
da = pattern.search(x)
if da:
    print(da.start())
else:
    print("No(")