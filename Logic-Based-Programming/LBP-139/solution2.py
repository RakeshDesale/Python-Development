# Using Function

# Solution:

def sortArr(L):
    for i in range(0,len(L)//2):
        for j in range(i+1,len(L)//2):
            if L[i]>L[j]:
                L[i],L[j] = L[j],L[i]
    return L


n = int(input())
L = sortArr([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
