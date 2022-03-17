# Using Function

# Solution:

def updateElementOnPosition(L,loc,ele):
    for i in range(len(L)):
        if i==loc:
            L[i] = ele
            break
    return L

n = int(input())
L = [int(i) for i in input().split()]
loc = int(input())
res = updateElementOnPosition(L,loc,int(input()))
for i in res:
    print(i,end=' ')
