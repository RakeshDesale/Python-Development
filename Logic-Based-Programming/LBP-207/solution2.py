# Using Function

# Solution:

def matrixColSum(L):
    for i in range(3):
        sum = 0
        for j in range(3):
            sum = sum + L[j][i]
        print(sum)

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
matrixColSum(L)
