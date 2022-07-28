# Using Function

# Optimized Solution:

def printSqr(L):
    for i in range(3):
        for j in range(3):
            print(L[i][j] * L[i][j], end=' ')
        print()

printSqr([[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]])
