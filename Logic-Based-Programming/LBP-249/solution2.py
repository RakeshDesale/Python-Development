# Optimized Solution:

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
for i in range(3):
    for j in range(3):
        print(str(L[i][j])[::-1], end=' ')
    print()
