# Another Way Using Function

# Solution:

def updateElementOnPosition(L,loc,ele):
    for i in range(len(L)):
        if i==loc:
            L[i] = ele
            break
    for i in L:
        print(i,end=' ')

n = int(input())
L = [int(i) for i in input().split()]
loc = int(input())
updateElementOnPosition(L,loc,int(input()))
