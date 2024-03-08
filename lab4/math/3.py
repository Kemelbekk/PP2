import math
def san(n,l):
    area = 0.25*n *(l**2)*(1/math.tan(math.pi/n))
    return area
a = int(input())
b = int(input())
c = san(a,b)
print(int(c))