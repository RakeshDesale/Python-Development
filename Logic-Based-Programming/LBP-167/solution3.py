# Using Function

# Solution:

import math
def countZero(n):
    count = 0
    while n!=0:
        if n%10 == 0:
            count += 1
        else:
            break
        n = n//10
    return count

n = int(input())
print(countZero(math.factorial(n)))
