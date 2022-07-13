# Using Function

# Solution:

def mulMatrix(L1, L2, L3):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                L3[i][j] = L3[i][j] + (L1[i][k] * L2[k][j])
    return L3

L1 = []
L2 = []
L3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    L1.append([int(i) for i in input().split()])
for i in range(3):
    L2.append([int(i) for i in input().split()])
L3 = mulMatrix(L1, L2, L3)
for i in range(3):
    for j in range(3):
        print(L3[i][j], end=' ')
    print()
