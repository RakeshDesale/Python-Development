# Solution:

L = []
prod = 1
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    for j in range(3):
        if i == j:
            prod *= L[i][j]
print(prod)
