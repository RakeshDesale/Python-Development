# Using Core Logic

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1,n):
        if L[i] > L[j]:
            L[i],L[j] = L[j],L[i]
print(L[n-3]+L[1])
