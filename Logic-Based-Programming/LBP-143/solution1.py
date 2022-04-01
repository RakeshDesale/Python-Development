# Solution:

def arrRange(n,m):
    L = []
    for i in range(n,m+1):
        L.append(i)
        print(i,end=' ')

n = int(input())
m = int(input())
if n>m:
    print(n)
else:
    arrRange(n,m)
