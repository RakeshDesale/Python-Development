# Without Using Function

# Solution:

n = int(input())
m = int(input())
L = []
if n>m:
    print (n)
else:
    for i in range(n,m+1):
        L.append(i)
        print(i,end=' ')
