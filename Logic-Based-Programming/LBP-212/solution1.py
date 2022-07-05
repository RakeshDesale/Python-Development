# Solution:

L = []
prod = 1
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    prod *= L[i][3 - i - 1]
print(prod)
