# Using Function

# Solution:

def identityMatrix(L):
    flag = True
    for i in range(3):
        for j in range(3):
            if i == j and L[i][j] != 1:
                flag = False
                break
            if i != j and L[i][j] != 0:
                flag = False
                break
    return flag

L = []
for i in range(3):
    L.append([int(i) for i in input().split()])
print("Yes" if identityMatrix(L) else "No")
