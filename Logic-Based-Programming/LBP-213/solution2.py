# Another Approach

# Solution:

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    for j in range(3):
        for k in range(j + 1, 3):
            if L[i][j] > L[i][k]:
                L[i][j], L[i][k] = L[i][k], L[i][j]
print(L[2][2])