# Using Function

# Solution:

import math

def arrToMatrix(L,m):
    k = 0
    for i in range(m):
        for j in range(m):
            print(L[k], end=' ')
            k += 1
        print()

n = int(input())
L = [int(i) for i in input().split()]
m = (int)(math.sqrt(n))
arrToMatrix(L,m)
