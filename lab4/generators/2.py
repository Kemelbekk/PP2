def san(n):
    for item in range(1, n+1):
        if item % 2 == 0:
            yield item
a = int(input())
b = san(a)
print(', '.join(str(x) for x in b))