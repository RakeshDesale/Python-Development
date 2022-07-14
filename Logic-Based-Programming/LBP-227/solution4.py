# Using Core Logic

# Solution:

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
for i in range(3):
    for j in range(3):
        for k in range(j + 1, 3):
            if(L[i][j] > L[i][k]):
                L[i][j], L[i][k] = L[i][k], L[i][j]
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
