# Solution:

L1 = []
L2 = []
L3 = []
for i in range(3):
    L1.append([int(i) for i in input().split()])
for i in range(3):
    L2.append([int(i) for i in input().split()])
for i in range(3):
    res = []
    for j in range(3):
        res.append(L1[i][j] + L2[i][j])
    L3.append(res)
for i in range(3):
    for j in range(3):
        print(L3[i][j], end=' ')
    print()
