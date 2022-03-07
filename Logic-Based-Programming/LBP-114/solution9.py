# Using Function and Sort Method (Reverse Approach)

# Solution:

def minElement(L):
    L.sort(reverse=True)
    return L[n-1]

n = int(input())
print(minElement([int(i) for i in input().split()]))
