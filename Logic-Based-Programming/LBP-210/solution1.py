# Solution:

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print(L[0][0] + L[2][2])
