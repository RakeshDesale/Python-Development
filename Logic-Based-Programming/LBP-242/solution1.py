# Solution:

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
sum = 0
for i in range(3):
    if i % 2 != 0:
        for j in range(3):
            sum = sum + L[i][j]
print(sum)
