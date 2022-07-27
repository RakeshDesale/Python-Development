# Using Function

# Optimized Solution:

def symmetricMat(L):
    count = 0
    for i in range(3):
        for j in range(3):
            if L[i][j] == L[j][i]:
                count += 1
    return count == 9

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
print("Yes" if symmetricMat([L1, L2, L3]) else "No")
