# Another Approach Using Function

# Solution:

def incArrEle(L):
    for i in range(len(L)):
        L[i] = L[i]+1
    return L

n = int(input())
L = incArrEle([int (i) for i in input().split()])
for i in L:
    print(i,end=' ')
