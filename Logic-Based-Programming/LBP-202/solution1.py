# Solution:

n = int(input())
m = int(input())
L = []
sum = 0
if ((n >= 1 and n <= 5) and (m >= 1 and m <= 5)):
    for i in range(n):
        L.append([int(i) for i in input().split()])
    for i in range(n):
        for j in range(m):
            sum = sum + L[i][j]
    print(sum)
else:
    pass
