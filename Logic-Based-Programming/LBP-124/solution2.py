# Using Function

# Solution:

def delElement(L,ele):
    if ele in L:
        L.remove(ele)
        for i in L:
            print(i,end=' ')
    else:
        print(-1)

n = int(input())
L = [int(i) for i in input().split()]
delElement(L,int(input()))
