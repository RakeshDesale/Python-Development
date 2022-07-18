# Using Function and Using Core Concept

# Solution:

def sortColEleDesc(L):
    LL = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            LL[i][j] = L[j][i]
    for i in range(3):
        for j in range(3):
            for k in range(j + 1, 3):
                if LL[i][j] < LL[i][k]:
                    LL[i][j], LL[i][k] = LL[i][k], LL[i][j]
    return LL

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = sortColEleDesc([L1, L2, L3])
for i in range(3):
    for j in range(3):
        print(L[j][i], end=' ')
    print()
