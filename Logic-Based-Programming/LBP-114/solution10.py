# Using Function and Python's Standard Sorted Method

# Solution:

def minElement(L):
    m=sorted(L)
    return m[1-1]

n = int(input())
print(minElement([int(i) for i in input().split()]))
