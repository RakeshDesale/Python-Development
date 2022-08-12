# Using Function

# Solution:

def sumOfEvenIndexedCols(L):
    sum = 0
    for i in range(3):
        for j in range(3):
            if j % 2 == 0:
                sum = sum + L[i][j]
    return sum

print(sumOfEvenIndexedCols([[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]))
