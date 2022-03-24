# Using Function

# Solution:

def arrSort(L):
    L.sort()
    return L

n = int(input())
L = arrSort([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
