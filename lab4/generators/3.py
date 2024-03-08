def san(n):
    for item in range(1, n + 1, 1):
        if item % 3 == 0 and item % 4 == 0:
            yield item

a = int(input("Enter a number: "))
b = san(a)
for x in b:
    print(x)
