def san(t):
    return all(t)

x = input()
y = x.split()
bval = [bool(value) for value in y]
z = tuple(bval)

result = san(z)

print(result)