# Using Function

# Solution:

def printArray(l):
    for i in l:
        print(i,end=' ')

n=int(input())
printArray([int(i) for i in input().split()])
