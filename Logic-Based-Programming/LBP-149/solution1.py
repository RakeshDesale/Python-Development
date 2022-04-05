# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(1,n-1):
    if L[i]>L[i-1] and L[i]>L[i+1]:
        print(L[i],end=' ')
