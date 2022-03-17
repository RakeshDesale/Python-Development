# Using Core Logic

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
loc = int(input())
ele = int(input())
for i in range(n):
    if i==loc:
        L[i] = ele
        break;
for i in L:
    print(i,end=' ')
