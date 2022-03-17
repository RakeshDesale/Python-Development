# Using Function

# Solution:

def updateElementOnPosition(L,loc,ele):
    L[loc] = ele
    return L

n = int(input())
L = [int(i) for i in input().split()]
loc = int(input())
ele = int(input())
res = updateElementOnPosition(L,loc,ele)
for i in res:
    print(i,end=' ')
