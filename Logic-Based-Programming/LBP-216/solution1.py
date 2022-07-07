# Solution:

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    min = L[i][0]
    for j in range(3):
        if min > L[i][j]:
            min = L[i][j]
    print(min)
