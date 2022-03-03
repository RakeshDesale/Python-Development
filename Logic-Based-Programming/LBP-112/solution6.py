# Another Approach Using Function

# Solution:

def searchElement(L,key):
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            if(L[i] > L[j]):
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    if key in L:
        return L.index(key)
    else:
        return -1

n = int(input())
L = [int(i) for i in input().split()]
print(searchElement(L,int(input())))
