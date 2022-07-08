# Using Function

# Solution:

def sumDiagonal(L):
    sum = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                sum = sum + L[i][j]
    return sum

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(sumDiagonal(L))
