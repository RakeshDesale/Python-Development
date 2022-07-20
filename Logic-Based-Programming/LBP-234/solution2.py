# Using Function

# Solution:

def interchangeDiagonal(L):
    for i in range(3):
        L[i][i], L[i][3 - i -1] = L[i][3 - i - 1], L[i][i]
    return L

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = interchangeDiagonal([L1, L2, L3])
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
