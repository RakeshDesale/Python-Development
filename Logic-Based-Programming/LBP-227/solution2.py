# Another Approach

# Solution:

L1 = sorted([int(i) for i in input().split()])
L2 = sorted([int(i) for i in input().split()])
L3 = sorted([int(i) for i in input().split()])
L = [L1, L2, L3]
for i in range(3):
    for j in range(3):
        print(L[i][j], end=' ')
    print()
