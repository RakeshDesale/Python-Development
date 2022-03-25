# Solution:

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in range(n):
    if i%2!=0:
        sum = sum + L[i]
print(sum)
