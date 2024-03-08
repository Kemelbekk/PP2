import re

pattern = re.compile("[a-z]_")
x = str(input())
matches = pattern.findall(x)
print(matches)