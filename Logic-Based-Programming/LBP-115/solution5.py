# Using Function

# Solution:

def maxminDiff(L):
    return max(L)-min(L)

n = int(input())
print(maxminDiff([int(i) for i in input().split()]))
