# Solution:

import math
n = int(input())
L = [int(i) for i in input().split()]
m = (int)(math.sqrt(n))
k = 0
for i in range(m):
    for j in range(m):
        print(L[k], end=' ')
        k += 1
    print()
