# Using Function

# Optimized Solution:

import math

def isStrong(n):
    temp=n
    sum=0
    while(n!=0):
        d = n%10
        sum = sum+math.factorial(d)
        n = n//10
    return temp==sum

n = int(input())
print(sum([int(i) for i in input().split() if isStrong(int(i))]))
