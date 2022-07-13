# Using In built sorted Method

# Solution:

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
LL = []
for i in range(3):
    for j in range(3):
        LL.append(L[i][j])
LL = sorted(LL)
k = 0
for i in range(3):
    for j in range(3):
        L[i][j] = LL[k]
        k += 1
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
