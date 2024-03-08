import time
import math

def sqrf(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    return result
num = float(input("Enter a number: "))

milli = int(input("Enter milliseconds: "))

result = sqrf(num, milli)
print(result)