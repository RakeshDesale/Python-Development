# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in L[::-1]:
    print(i,end=' ')
