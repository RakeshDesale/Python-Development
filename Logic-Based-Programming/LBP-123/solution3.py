# Another Approach Using Function

# Solution:

def delEleFromPos(L,pos):
    L.pop(pos)
    return L

n = int(input())
L = [int(i) for i in input().split()]
L = delEleFromPos(L,int(input()))
for i in L:
    print(i,end=' ')
