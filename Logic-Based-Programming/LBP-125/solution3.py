# Another Approach Using Function

# Solution:

def updateElement(L,oldele,newele):
    for i in range(len(L)):
        if L[i] == oldele:
            L[i] = newele
    return L

n = int(input())
L = [int(i) for i in input().split()]
oldele = int(input())
res = updateElement(L,oldele,int(input()))
for i in res:
    print(i,end=' ')
