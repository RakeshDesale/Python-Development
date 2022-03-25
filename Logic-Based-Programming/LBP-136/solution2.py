# Using Function

# Solution:

def indexSum(L,n):
    low = 0
    high = n-1
    while(low <= high):
        print(L[low]+L[high],end=' ')
        low += 1
        high -=1
    
n = int(input())
indexSum([int(i) for i in input().split()],n)
