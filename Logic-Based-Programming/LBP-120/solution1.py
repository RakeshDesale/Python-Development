# Solution:

n = int(input())
L = [int(i) for i in input().split()]
ele = int(input())
L.append(ele)
for i in L:
    print(i,end=' ')
