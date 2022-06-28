# Solution:

L = []
sum = 0
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    for j in range(3):
        factors = 0
        for k in range(1, L[i][j] + 1):
            if(L[i][j] % k == 0):
                factors += 1
        if factors == 2:
            sum = sum + L[i][j]
print(sum)
