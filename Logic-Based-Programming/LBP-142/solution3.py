# Using Function

# Solution:

def multipleArr(m,n):
    L = []
    for i in range(1,n+1):
        L.append(m*i)
    for i in L:
        print(i,end=' ')

m = int(input())
multipleArr(m,int(input()))
