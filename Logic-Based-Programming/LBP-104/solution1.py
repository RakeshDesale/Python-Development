# Solution:

n = int(input())
l = [int(i) for i in input().split()]
sum = 0
for i in l:
    if i%2!=0:
        sum = sum + i
print(sum)
