# Another Approach Using Function

# Solution:

def delLastEle(L):
    L.pop(-1)
    return L
        
n = int(input())
L = delLastEle([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
