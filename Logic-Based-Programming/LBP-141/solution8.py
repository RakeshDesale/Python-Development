# Using Core Logic and Using Function

# Solution:

def rearrangeArr(L):
    for i in range(n):
        for j in range(i+1,n):
            if L[i]>L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
    return L

n = int(input())
L = rearrangeArr([int(i) for i in input().split()])
low = 0
high = n-1
while(low <= high):
    print(L[low],L[high],end=' ')
    low += 1
    high -= 1
