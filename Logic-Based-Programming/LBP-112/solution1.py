# Solution:

n = int(input())
L = [int(i) for i in input().split()]
key = int(input())
L.sort()
if key in L:
    print(L.index(key))
else:
    print(-1)
