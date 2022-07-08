# Solution:

L = []
flag = True
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    for j in range(3):
        if i == j and L[i][j] != 1:
            flag = False
            break
        if i != j and L[i][j] != 0:
            flag = False
            break
print("Yes" if flag else "No")
