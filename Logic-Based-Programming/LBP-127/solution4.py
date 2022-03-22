# Another Approach Using Function

# Solution:

def arrReverse(L):
    L.reverse()
    return L

n = int(input())
L = arrReverse([int(i) for i in input().split()])
for i in L:
    print(i,end=' ')
