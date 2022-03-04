# Traditional Way

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in range(0,len(L)):
    for j in range(i+1,len(L)):
        if L[i]>L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
print(L[n-1])
