# Using Function

# Solution:

def rearrangeArr(L):
    L.sort()
    return L
    
n = int(input())
L = rearrangeArr([int(i) for i in input().split()])
low = 0
high = n-1
while(low <= high):
    print(L[low],L[high],end=' ')
    low += 1
    high -= 1
