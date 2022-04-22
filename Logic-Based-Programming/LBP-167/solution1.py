# Using Math Module

# Solution:

import math
n = int(input())
f = math.factorial(n)
count = 0
while f!=0:
    if f%10 == 0:
        count += 1
    else:
        break
    f = f//10
print(count)
