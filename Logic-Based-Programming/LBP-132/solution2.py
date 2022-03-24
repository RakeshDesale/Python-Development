# Using Function

# Solution:

def replaceArrEle(L,n):
    for i in range(0,n):
        m = max(L[i:])
        L[i] = m
    return L

n = int(input())
L = replaceArrEle([int(i) for i in input().split()],n)
for i in L:
    print(i,end=' ')
