# Using Core Logic and Using Function

# Solution:

def secondMax(L,n):
    for i in range(n):
        for j in range(i+1,n):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L[n-2]
    
n = int(input())
print(secondMax([int(i) for i in input().split()],n))
