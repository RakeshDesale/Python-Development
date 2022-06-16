# Using Core Logic

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1,n):
        if L[i] > L[j]:
            L[i],L[j] = L[j],L[i]
for i in range(n//2):
    print(L[i],end=' ')
for i in range(n-1,n//2-1,-1):
    print(L[i],end=' ')
