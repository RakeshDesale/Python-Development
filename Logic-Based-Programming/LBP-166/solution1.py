# Solution:

n,m = (int(i) for i in input().split())
for i in range(n):
    L = [int(i) for i in input().split()]
    print(max(L),end=' ')
