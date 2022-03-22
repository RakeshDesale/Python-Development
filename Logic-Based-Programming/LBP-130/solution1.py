# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L2 = []
for i in L:
    if i not in L2:
        L2.append(i)
for i in L2:
    print(i,end=' ')
