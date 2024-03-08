import re

x = str(input())
da = re.sub("\s",",",x)
print(da)