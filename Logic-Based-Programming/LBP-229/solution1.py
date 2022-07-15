# Solution:

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
LL = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        LL[i][j] = L[j][i]
for i in range(3):
    LL[i].sort()
for i in range(3):
    for j in range(3):
        print(LL[j][i], end=' ')
    print()
