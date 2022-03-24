# Traditional Approach

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(0,n):
    for j in range(i+1,n):
        if L[i]>L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
for i in L:
    print(i,end=' ')
