# Reverse Approach Using Function

# Solution:

def maxElement(L):
    L.sort(reverse=True)
    return L[1-1]

n = int(input())
print(maxElement([int(i) for i in input().split()]))
