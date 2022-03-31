# Solution:

m = int(input())
n = int(input())
L = []
for i in range(1,n+1):
    L.append(m*i)
for i in L:
    print(i,end=' ')
