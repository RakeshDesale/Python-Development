# Optimized Solution:

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
count = 0
for i in range(3):
    for j in range(3):
        if L[i][j] == L[j][i]:
            count += 1
print("Yes" if count == 9 else "No")
