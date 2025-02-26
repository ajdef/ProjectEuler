#5. Alternate Solution
import math
def lcm(a, b):
    return abs(a*b)//math.gcd(a,b)

def smallestMultiple(n):
    result = 1                 
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

print(smallestMultiple(20))