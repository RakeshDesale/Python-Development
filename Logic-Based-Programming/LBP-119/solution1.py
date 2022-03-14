# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.insert(0,int(input()))
for i in L:
    print(i,end=' ')
