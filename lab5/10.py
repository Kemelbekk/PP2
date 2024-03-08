def cts(ccs):
    scs = ''
    for char in ccs:
        if char.isupper():
            scs += '_' + char.lower()
        else:
            scs += char
    if scs.startswith('_'):
        scs = scs[1:]
    return scs

ccs = "NFJFjnBJBjbjBJjbbj"
scs = cts(ccs)
print(scs)