# Traditional Approach Using Function

# Solution:

def searchElement(L,key):
    index = -1
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            if (L[i] > L[j]):
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    
    for i in range(0,len(L)):
        if key == L[i]:
            index = i
            break
    return index

n = int(input())
L = [int(i) for i in input().split()]
print(searchElement(L,int(input())))
