# Using Function and Return Value

# Solution:

def multipleArr(m,n):
    L = []
    for i in range(1,n+1):
        L.append(m*i)
    return L

m = int(input())
L = multipleArr(m,int(input()))
for i in L:
    print(i,end=' ')
