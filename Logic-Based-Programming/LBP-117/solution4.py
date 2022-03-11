# Using Function

# Solution:

def secondMin(L):
    L.sort()
    return L

n = int(input())
L = secondMin([int(i) for i in input().split()])
print(L[2-1])
