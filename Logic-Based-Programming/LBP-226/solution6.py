# Using Function and Using Core Logic

# Solution:

def sortEleDesc(L):
    LL = []
    for i in range(3):
        for j in range(3):
            LL.append(L[i][j])
    for i in range(len(LL)):
        for j in range(i + 1,len(LL)):
            if LL[i] < LL[j]:
                LL[i], LL[j] = LL[j], LL[i]
    k = 0
    for i in range(3):
        for j in range(3):
            L[i][j] = LL[k]
            k += 1
    return L

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1,L2,L3]
L = sortEleDesc(L)
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
