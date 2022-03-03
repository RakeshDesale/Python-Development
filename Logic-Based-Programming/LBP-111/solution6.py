# Traditional Approach Using Function

# Solution:

def sortArrDesc(L):
    temp = 0
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            if (L[i] < L[j]):
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

n = int(input())
L = sortArrDesc([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
