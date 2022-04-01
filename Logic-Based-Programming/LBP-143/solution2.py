# Another Approach

# Solution:

def arrRange(n,m):
    L = []
    for i in range(n,m+1):
        L.append(i)
    return L

n = int(input())
m = int(input())
if n>m:
    print(n)
else:
    L = arrRange(n,m)
    for i in L:
        print(i,end=' ')
