# Using Function

# Solution:

def insertElement(ele,L):
    L.insert(0,ele)
    return L

n = int(input())
L = [int(i) for i in input().split()]
ele = insertElement(int(input()),L)
for i in L:
    print(i,end=' ')
