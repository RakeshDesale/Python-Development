# Using Function and Sort Method

# Solution:

def minElement(L):
    L.sort()
    return L[1-1]

n = int(input())
print(minElement([int(i) for i in input().split()]))
