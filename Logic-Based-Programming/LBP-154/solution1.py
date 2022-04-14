# Solution:

n = int(input())
sd,ed = (int(i) for i in input().split())
L = [int(i) for i in input().split()]
for i in L:
    if abs(i)>=sd and abs(i)<=ed:
        print(i,end=' ')
