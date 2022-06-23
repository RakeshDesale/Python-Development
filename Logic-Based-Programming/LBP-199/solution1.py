# Solution:

n = int(input())
L = [int(i) for i in input().split()]
k = int(input())
sum = 0
for i in L:
    sum = sum + i // k
print(sum)
