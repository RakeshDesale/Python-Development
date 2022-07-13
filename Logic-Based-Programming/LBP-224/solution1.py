# Solution:

L1 = []
L2 = []
L3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    L1.append([int(i) for i in input().split()])
for i in range(3):
    L2.append([int(i) for i in input().split()])
for i in range(3):
    for j in range(3):
        for k in range(3):
            L3[i][j] = L3[i][j] + (L1[i][k] * L2[k][j])
for i in range(3):
    for j in range(3):
        print(L3[i][j], end=' ')
    print()
