# Using Function

# Solution:

import math
def gcdVal(num1,num2):
    return math.gcd(num1,num2)

num1,num2 = (int(i) for i in input().split())
print(gcdVal(num1,num2))
