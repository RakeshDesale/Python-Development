# Using Function

# Optimized Solution:

def sortArrDesc(L):
    return (sorted(L,reverse=True))

n = int(input())
L = sortArrDesc([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
    
