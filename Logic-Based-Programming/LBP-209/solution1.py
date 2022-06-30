# Solution:

L = []
sum = 0
for i in range(3):
    L.append([int(i) for i in input().split()])
for i in range(3):
    sum = sum + L[i][3 - i - 1]
print(sum)
