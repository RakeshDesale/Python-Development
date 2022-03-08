# Another Approach Using Function

# Solution:

def maxminDiff(L,n):
    L.sort()
    return (L[n-1]-L[1-1])

n = int(input())
print(maxminDiff([int(i) for i in input().split()],n))
