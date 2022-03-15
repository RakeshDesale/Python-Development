# Another Approach Using Function

# Solution:

def delElement(L,ele):
    L.remove(ele)
    return L

n = int(input())
L = [int(i) for i in input().split()]
ele = int(input())
if ele in L:
    L = delElement(L,ele)
    for i in L:
        print(i,end=' ')
else:
    print(-1)
