# Another Approach Using Function

# Solution:

def maxElement(L,n):
    m=sorted(L)
    return m[n-1]

n = int(input())
print(maxElement([int(i) for i in input().split()],n))
