# Using Function

# Solution:

def kShortExeTime(L,k):
    L.sort()
    return L[k-1]

n = int(input())
k = int(input())
print(kShortExeTime([int(i) for i in input().split()],k))
