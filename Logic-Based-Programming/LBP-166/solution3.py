# Using Function and No Return Value

# Solution:

def maxRevenue(L,n):
    print(max(L),end=' ')
    
n,m = (int(i) for i in input().split())
for i in range(n):
    L = [int(i) for i in input().split()]
    maxRevenue(L,n)
