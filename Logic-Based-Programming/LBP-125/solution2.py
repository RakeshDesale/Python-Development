# Using Function

# Solution:

def updateElement(L,oldele,newele):
    for i in range(len(L)):
        if L[i] == oldele:
            L[i] = newele
    for i in L:
        print(i,end=' ')

n = int(input())
L = [int(i) for i in input().split()]
oldele = int(input())
updateElement(L,oldele,int(input()))
