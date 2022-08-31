# Optimize Solution:

L = [[int(i) for i in input().split()], [int(i) for i in input().split()], [int(i) for i in input().split()]]
count = 0
for i in range(3):
    for j in range(3):
        for k in str(L[i][j]):
            if k in '2357':
                count += 1
print(count)
