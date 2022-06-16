# Using Inbuilt Sorted Method

# Solution:

n = int(input())
L = sorted([int(i) for i in input().split()])
for i in range(n//2):
    print(L[i],end=' ')
for i in range(n-1,n//2-1,-1):
    print(L[i],end=' ')
