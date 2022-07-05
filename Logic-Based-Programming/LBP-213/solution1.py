# Solution:

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
max = L[0][0]
for i in range(3):
    for j in range(3):
        if max < L[i][j]:
            max = L[i][j]
print(max)
