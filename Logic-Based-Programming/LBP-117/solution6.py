# Using Function

# Solution:

def secondMin(L):
    L.sort()
    return L[2-1]

n = int(input())
print(secondMin([int(i) for i in input().split()]))
