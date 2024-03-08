import math
def san(a,b,c):
    area = 0.5*c*(a + b)
    return area
upbase = int(input())
downbase = int(input())
height = int(input())
trap = san(upbase,downbase,height)
print(trap)