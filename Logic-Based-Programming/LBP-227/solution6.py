# Using Function and Using Inbuilt sorted Method

# Solution:

def sortRowEle(L):
    for i in range(3):
        L[i] = sorted(L[i])
    return L

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = sortRowEle([L1, L2, L3])
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
