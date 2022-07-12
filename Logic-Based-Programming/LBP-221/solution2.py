# Using Function

# Solution:

def compareMatrix(L1, L2):
    flag = True
    for i in range(3):
        for j in range(3):
            if L1[i][j] != L2[i][j]:
                flag = False
                break
    return flag

L1 = []
L2 = []
for i in range(3):
    L1.append([int(i) for i in input().split()])
for i in range(3):
    L2.append([int(i) for i in input().split()])
print("Yes" if compareMatrix(L1, L2) else "No")
