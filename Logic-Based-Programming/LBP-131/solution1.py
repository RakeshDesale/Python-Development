# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort()
for i in L:
    print(i,end=' ')
