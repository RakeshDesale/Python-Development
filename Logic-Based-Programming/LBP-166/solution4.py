# Using Function and Return Value

# Solution:

def maxRevenue(L):
    return max(L)
    
n,m = (int(i) for i in input().split())
for i in range(n):
    L = [int(i) for i in input().split()]
    print(maxRevenue(L),end=' ')
