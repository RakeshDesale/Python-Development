# Traditional Approach Using Function

# Solution:

def arrSort(L,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if L[i]>L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

n = int(input())
L = arrSort([int(i) for i in input().split()],n)
for i in L:
    print(i,end=' ') 
