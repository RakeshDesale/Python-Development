# Optimized Solution:

n = int(input())
L = (sorted([int(i) for i in input().split()],reverse=True))
for i in L:
    print(i,end=' ')
