# Solution:

n = int(input())
a = [int(i) for i in input().split()]
sum = 0
for i in a:
    sum = sum + (i * (i + 1))
print(sum)
