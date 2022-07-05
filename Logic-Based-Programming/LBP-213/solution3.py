# Using Function

# Solution:

def maxEle(L):
    max = L[0][0]
    for i in range(3):
        for j in range(3):
            if max < L[i][j]:
                max = L[i][j]
    return max

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(maxEle(L))
