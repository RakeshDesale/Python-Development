# Using Function

# Solution:

def delEleFromPos(L,pos):
    L.pop(pos)
    for i in L:
        print(i,end=' ')

n = int(input())
L = [int(i) for i in input().split()]
delEleFromPos(L,int(input()))
