def squares(n,m):
    for item in range(n, m+1, 1):
        yield item**2
a = int(input())
b = int(input())
c = squares(a,b)
for x in c:
    print(x)
