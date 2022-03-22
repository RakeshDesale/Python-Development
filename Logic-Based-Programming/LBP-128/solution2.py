# Using Function

# Solution:

def incArrEle(L):
    for i in L:
        print(i+1,end=' ')

n = int(input())
incArrEle([int (i) for i in input().split()])
