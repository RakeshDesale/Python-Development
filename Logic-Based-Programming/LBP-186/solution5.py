# Using Function and Using Inbuilt sorted Method

# Solution:

def halfAscDesc(L):
    L = sorted(L)
    return L

n = int(input())
L = halfAscDesc([int(i) for i in input().split()])
for i in range(n//2):
    print(L[i],end=' ')
for i in range(n-1,n//2-1,-1):
    print(L[i],end=' ')
