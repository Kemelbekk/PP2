import re

pattern = re.compile("[A-Z][a-z]+")
x = str(input())
matches = pattern.findall(x)
print(matches)