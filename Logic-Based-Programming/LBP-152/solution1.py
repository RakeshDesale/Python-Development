# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in L:
    if i%2==0:
        print(i,end=' ')
for i in L:
    if i%2!=0:
        print(i,end=' ')
