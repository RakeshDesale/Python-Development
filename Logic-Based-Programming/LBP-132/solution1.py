# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(0,n):
    m=max(L[i:])
    L[i] = m
for i in L:
    print(i,end=' ')
