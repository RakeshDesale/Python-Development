# Using Function

# Solution:

def scalarMatMul(L, m):
    for i in range(3):
        for j in range(3):
            print(L[i][j] * m, end=' ')
        print()

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
scalarMatMul(L, int(input()))
