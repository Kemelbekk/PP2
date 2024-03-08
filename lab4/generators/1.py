def san(a):
    for item in range(1, a+1, 1):
        yield item**2
n = int(input())
m = san(n)
for x in m:
    print(x)