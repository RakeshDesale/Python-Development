# Solution:

n = int(input())
L = [int(i) for i in input().split()]
loc = int(input())
ele = int(input())
L[loc] = ele
for i in L:
    print(i,end=' ')
