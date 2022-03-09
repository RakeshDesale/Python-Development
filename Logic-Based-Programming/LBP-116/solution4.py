# Using Function

# Solution:

def secondMax(L):
    L.sort()
    return L[n-2]

n = int(input())
print(secondMax([int(i) for i in input().split()]))
