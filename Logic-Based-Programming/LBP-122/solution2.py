# Using Function

# Solution:

def delLastEle(L):
    L.pop(-1)
    for i in L:
        print(i,end=' ')
        
n = int(input())
delLastEle([int(i) for i in input().split()])
