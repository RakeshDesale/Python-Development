# Solution:

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    for j in range(3):
        print(L[j][i],end=' ')
    print()
