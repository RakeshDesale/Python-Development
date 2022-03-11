# Using Core Concept and Using Function

# Solution:

def secondMin(L):
    for i in range(n):
        for j in range(i+1,n):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
    return L[2-1]

n = int(input())
print(secondMin([int(i) for i in input().split()]))
