# Another Approach Using Function

# Solution:

def maxElement(L,n):
    L.sort()
    return L[n-1]

n = int(input())
print(maxElement([int(i) for i in input().split()],n))
