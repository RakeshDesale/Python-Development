# Using Function

# Solution:

def oppDiagonalProd(L):
    prod = 1
    for i in range(3):
        prod *= L[i][3 - i - 1]
    return prod

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(oppDiagonalProd(L))
