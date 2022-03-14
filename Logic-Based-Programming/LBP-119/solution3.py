# Another Approach Using Function

# Solution:

def insertElement(L):
    L.insert(0,int(input()))
    return L

n = int(input())
L = insertElement([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
