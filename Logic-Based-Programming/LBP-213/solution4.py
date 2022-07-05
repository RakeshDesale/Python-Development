# Another Approach Using Function

# Solution:

def maxEle(L):
    for i in range(3):
        for j in range(3):
            for k in range(j + 1, 3):
                if L[i][j] > L[i][k]:
                    L[i][j], L[i][k] = L[i][k], L[i][j]
    return L[2][2]

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(maxEle(L))
