# Another Approach

# Solution:

n = int(input())
L = sorted([int(i) for i in input().split()])
print(L[n-3]+L[1])
