# Solution:

n = int(input())
L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
for i in range(n):
    L1[i] = L1[i]+L2[i]
for i in L1:
    print(i,end=' ')
