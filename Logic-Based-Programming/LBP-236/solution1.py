# Solution:

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
flag = True
for i in range(3):
    for j in range(3):
        if j > i and L[i][j] != 0:
            flag = False
            break
print("Yes" if flag else "No")
