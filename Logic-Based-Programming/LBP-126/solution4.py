# Another Approach Using Function

# Solution:

def updateElementOnPosition(L,loc,ele):
    L[loc] = ele
    for i in L:
        print(i,end=' ')

n = int(input())
L = [int(i) for i in input().split()]
loc = int(input())
updateElementOnPosition(L,loc,int(input()))
