# Solution:

n = int(input())
print(sum([int(i) for i in input().split() if int(i)%10==3]))