# Using Function

# Solution:

def lastNElements(L,last):
    if last>len(L):
        print(0)
    else:
        for i in range(len(L)-last,len(L)):
            print(L[i],end=' ')

size = int(input())
L = [int(i) for i in input().split()]
lastNElements(L,int(input()))
