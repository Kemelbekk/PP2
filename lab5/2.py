import re

pattern = re.compile("ab{2,3}")

x = str(input())
matches = pattern.search(x)

if matches:
    print("available")
else:
    print("does not available")
