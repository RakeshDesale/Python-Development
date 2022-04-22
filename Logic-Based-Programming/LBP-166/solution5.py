# Using Function and Using Core Logic

# Solution:

def maxRevenue(L,n,m):
    for i in range(n):
        max = L[i][0]
        for j in range(m):
            if max < L[i][j]:
                max = L[i][j]
        print(max,end=' ')

n,m = (int(i) for i in input().split())
L = []
for i in range(n):
    L.append([int(i) for i in input().split()])
maxRevenue(L,n,m)
