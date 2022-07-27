# Using Function

# Solution:

def symmetricMat(L):
    LL = []
    flag = True
    for i in range(3):
        LL.append(L[i])
    for i in range(3):
        for j in range(3):
            if L[i][j] != LL[j][i]:
                flag = False
                break
    return flag

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
print("Yes" if symmetricMat([L1, L2, L3]) else "No")
