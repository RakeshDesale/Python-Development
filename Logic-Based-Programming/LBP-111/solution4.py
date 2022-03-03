# Using Function

# Solution:

def sortArrDesc(L):
    L.sort(reverse=True)
    return L

n = int(input())
L = sortArrDesc([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
