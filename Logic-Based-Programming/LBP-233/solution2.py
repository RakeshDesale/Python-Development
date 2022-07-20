# Using Function

# Solution:

def swapCols(L):
    for i in range(3):
        L[i][m - 1], L[i][n - 1] = L[i][n - 1], L[i][m - 1]
    return L

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
m = int(input())
n = int(input())
L = swapCols([L1, L2, L3])
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
