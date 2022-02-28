# Optimized Solution:

n = int(input())
print(sum([int(i) for i in input().split() if int(i)%2!=0]))
