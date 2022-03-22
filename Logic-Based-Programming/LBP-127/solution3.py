# Using Function

# Solution:

def arrReverse(L):
    for i in L[::-1]:
        print(i,end=' ')

n = int(input())
arrReverse([int(i) for i in input().split()])
