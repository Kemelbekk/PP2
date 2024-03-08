def san(n):
    for item in range(n, -1, -1):
            yield item
a = int(input())
b = san(a)
for x in b:
    print(x)

