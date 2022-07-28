# Optimized Solution:

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
for i in range(3):
    for j in range(3):
        print(L[i][j] * L[i][j], end=' ')
    print()
