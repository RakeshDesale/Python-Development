# Using Function

# Solution:

def minEle(L):
    min = L[0][0]
    for i in range(3):
        for j in range(3):
            if min > L[i][j]:
                min = L[i][j]
    return min

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(minEle(L))
