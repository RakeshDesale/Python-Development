# Using Function

# Solution:

def matrixOddSum(L):
    sum = 0
    for i in range(3):
        for j in range(3):
            if (L[i][j] % 2 != 0):
                sum = sum + L[i][j]
    return sum

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(matrixOddSum(L))
