# Another Approach Using Function

# Solution:

import math

def isStrong(n):
    temp = n
    sum = 0
    while (n!=0):
        d = n%10
        sum = sum + math.factorial(d)
        n = n//10
    return temp==sum

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in L:
    if isStrong(i):
        sum = sum+i
print(sum)
