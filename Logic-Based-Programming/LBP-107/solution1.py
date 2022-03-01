# Solution:

import math

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in L:
    factsum=0
    temp = i
    while(temp!=0):
        d = temp%10
        factsum = factsum+math.factorial(d)
        temp = temp//10
    if(i==factsum):
        sum = sum+i
print(sum)
