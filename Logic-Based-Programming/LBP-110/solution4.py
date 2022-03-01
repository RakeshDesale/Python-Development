# Using Function

# Solution:

def sortArrAsc(l):
    l.sort()
    for i in l:
        print(i,end=' ')

n = int(input())
sortArrAsc([int(i) for i in input().split()])
