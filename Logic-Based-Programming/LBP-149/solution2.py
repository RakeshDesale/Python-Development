# Using Function

# Solution:

def strictGreat(L):
    for i in range(1,len(L)-1):
        if L[i]>L[i-1] and L[i]>L[i+1]:
            print(L[i],end=' ')

n = int(input())
strictGreat([int(i) for i in input().split()])
