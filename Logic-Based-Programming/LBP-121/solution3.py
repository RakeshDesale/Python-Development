# Another Way Using Function

# Solution:

def delFirstEle(L):
    L.pop(0)
    return L
    
n = int(input())
L = delFirstEle([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
