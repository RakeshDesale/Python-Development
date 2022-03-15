# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.pop(-1)
for i in L:
    print(i,end=' ')
