# Using Function

# Solution:

def searchElement(L,n,key):
    index=-1
    for i in range(0,len(L)):
        if(L[i]==key):
            index=i
            break
    return index

n=int(input())
L=[int(i) for i in input().split()]
print(searchElement(L,n,int(input())))
