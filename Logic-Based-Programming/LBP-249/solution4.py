# Using Function

# Optimized Solution:

def rev(n):
    return str(n)[::-1]

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
for i in range(3):
    for j in range(3):
        print(rev(L[i][j]), end=' ')
    print()
