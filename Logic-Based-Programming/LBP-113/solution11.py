# Traditional Approach Using Function

# Solution:

def maxElement(L,n):
    for i in range(0,len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L[n-1]

n = int(input())
print(maxElement([int(i) for i in input().split()],n))
