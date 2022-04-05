# Using Core Logic

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1,n):
        if L[i]>L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
for i in range(n):
    if L[i]>0:
        print(L[i]+L[i+1])
        break
