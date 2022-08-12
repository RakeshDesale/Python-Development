# Using Function

# Solution:

def sumOfEvenIndexedRowCol(L):
    sum = 0
    for i in range(3):
        for j in range(3):
            if (i + j) % 2 == 0:
                sum = sum + L[i][j]
    return sum

print(sumOfEvenIndexedRowCol([[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]))
