# Using Function

# Solution:

def alternateSmall(L):
    L.sort()
    return L[n-3]+L[1]

n = int(input())
print(alternateSmall([int(i) for i in input().split()]))
