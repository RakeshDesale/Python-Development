# Using Function

# Solution:

def reverseArrEle(L):
    for i in L:
        print(i[::-1],end=' ')

n = int(input())
reverseArrEle([i for i in input().split()])
