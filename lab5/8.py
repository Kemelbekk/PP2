import re
x = str(input())
da = re.findall("[A-Z][^A-Z]*",x)
print(da)