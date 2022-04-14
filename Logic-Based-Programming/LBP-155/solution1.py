# Solution:

n = int(input())
k = int(input())
L = [int(i) for i in input().split()]
L.sort()
print(L[k-1])
