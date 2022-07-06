# Solution:

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
min = L[0][0]
for i in range(3):
    for j in range(3):
        if min > L[i][j]:
            min = L[i][j]
print(min)
