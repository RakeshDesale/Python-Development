# Using Third Array (List)

# Solution:

n = int(input())
L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = []
for i in range(n):
    L3.append(L1[i]+L2[i])
for i in L3:
    print(i,end=' ')
