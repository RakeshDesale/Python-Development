# Solution:

def printEven(L):
    for i in L:
        if i%2==0:
            print(i,end=' ')

n = int(input())
printEven([int(i) for i in input().split()])
