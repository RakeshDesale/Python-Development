# Solution:

n = int(input())
m = int(input())
L = []
if ((n >= 1 and n <= 5) and (m >= 1 and m <= 5)):
    for i in range(n):
        L.append([int(i) for i in input().split()])
    for i in range(n):
        for j in range(m):
            print(L[i][j],end=' ')
        print()
else:
    pass
