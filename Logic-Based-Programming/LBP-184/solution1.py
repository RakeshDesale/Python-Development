# Solution:

n = int(input())
L1 = [int(i) for i in input().split()]
L2 = L1.copy()
L1.sort()
count = 0
for i in range(n):
    if L1[i] == L2[i]:
        count += 1
print(count)
