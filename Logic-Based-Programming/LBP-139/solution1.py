# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(0,n//2):
    for j in range(i+1,n//2):
        if L[i]>L[j]:
            L[i],L[j] = L[j],L[i]
for i in L:
    print(i,end=' ')
