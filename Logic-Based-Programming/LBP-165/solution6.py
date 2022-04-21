# Using Function and Using Core Logic

# Solution:

def alternateSmall(L):
    for i in range(n):
        for j in range(i+1,n):
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
    return L[n-3]+L[1]

n = int(input())
print(alternateSmall([int(i) for i in input().split()]))
