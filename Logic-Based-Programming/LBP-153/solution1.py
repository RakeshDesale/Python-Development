# Solution:

n = int(input())
L = [int(i) for i in input().split()]
count = 0
for i in range(n):
    for k in range(1,L[i]+1):
        if k*k==L[i]:
            count += 1
print(count)
