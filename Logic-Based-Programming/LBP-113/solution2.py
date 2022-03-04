# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort()
print(L[n-1])
