# Using Function

# Solution:

def maxElement(L):
    return max(L)

n = int(input())
print(maxElement([int(i) for i in input().split()]))
