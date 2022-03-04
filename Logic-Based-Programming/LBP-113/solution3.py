# Reverse Approach

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort(reverse=True)
print(L[1-1])
