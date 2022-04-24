# Using Function

# Solution:

def matrixToArr(m):
    for i in range(m):
        L = [int(i) for i in input().split()]
        for j in L:
            print(j,end=' ')

m,n = (int(i) for i in input().split())
matrixToArr(m)
