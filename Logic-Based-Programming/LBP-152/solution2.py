# Using Function

# Solution:

def oddAfterEven(L):
    for i in L:
        if i%2==0:
            print(i,end=' ')
    for i in L:
        if i%2!=0:
            print(i,end=' ')

n = int(input())
oddAfterEven([int(i) for i in input().split()])
