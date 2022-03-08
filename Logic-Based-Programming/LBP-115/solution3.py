# Optimized Solution:

n = int(input())
L = sorted([int(i) for i in input().split()])
print(L[n-1]-L[1-1])
