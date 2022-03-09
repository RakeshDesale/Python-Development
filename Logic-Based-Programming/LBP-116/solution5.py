# Another Approach Using Function

# Solution:

def secondMax(L):
    L = sorted(L)
    return L[n-2]

n = int(input())
print(secondMax([int(i) for i in input().split()]))
