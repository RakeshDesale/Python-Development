# Traditional Approach Using Function

# Solution:

def maxminDiff(L,n):
    for i in range(n):
        for j in range(i+1,n):
            if L[i]>L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return (L[n-1]-L[1-1])

n = int(input())
print(maxminDiff([int(i) for i in input().split()],n))
