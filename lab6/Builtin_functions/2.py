x = str(input())
up = 0
lo = 0
for item in x:
    if ord(item) in range (97,123):
        lo += 1
    else:
        up += 1
print("The number of lower case letters are :", lo)
print("The number of upper case letters are :", up)