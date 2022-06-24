# Using Function

# Solution:

def matrixSum(L, n, m):
    sum = 0
    for i in range(n):
        for j in range(m):
            sum = sum + L[i][j]
    return sum

n = int(input())
m = int(input())
L = []
if ((n >= 1 and n <= 5) and (m >= 1 and m <= 5)):
    for i in range(n):
        L.append([int(i) for i in input().split()])
    print(matrixSum(L, n, m))
else:
    pass
