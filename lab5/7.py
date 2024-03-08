def san(s):
    slova = s.split('_')
    cw = [slova[0].lower()] + [word.capitalize() for word in slova[1:]]
    cc = ''.join(cw)
    return cc

scs = "snake_asan_example"
ccs = san(scs)
print(ccs)  