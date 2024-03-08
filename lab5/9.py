import re
x = str(input())
da = re.sub(r'(?<!^)(?=[A-Z])', ' ', x)
print(da)
