# Using Function

# Solution:

def sumOfEvenIndexedRows(L):
    sum = 0
    for i in range(3):
        if i % 2 != 0:
            for j in range(3):
                sum = sum + L[i][j]
    return sum

print(sumOfEvenIndexedRows([[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]))
