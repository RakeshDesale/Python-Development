# Another Approach

# Solution:

L1 = [int(i) for i in input().split()]
L2 = [int(i) for i in input().split()]
L3 = [int(i) for i in input().split()]
L = [L1, L2, L3]
counter = 0
for i in range(3):
    for j in range(3):
        if L[i][j] == 0:
            counter += 1
print("Yes" if counter >= 5 else "No")
