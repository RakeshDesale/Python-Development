# Using Function

# Solution:

def searchElement(L,key):
    L.sort()
    if key in L:
        return L.index(key)
    else:
        return -1

n = int(input())
L = [int(i) for i in input().split()]
print(searchElement(L,int(input())))
