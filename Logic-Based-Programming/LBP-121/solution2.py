# Using Function

# Solution:

def delFirstEle(L):
    L.pop(0)
    for i in L:
        print(i,end=' ')

n = int(input())
delFirstEle([int(i) for i in input().split()])
