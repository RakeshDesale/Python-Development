# Using Function and No Return Value

# Solution:

def reverseArrEle(L):
    for i in L:
        rev = 0
        while(i!=0):
            d = i%10
            rev = rev*10+d
            i = i//10
        print(rev,end=' ')

n = int(input())
reverseArrEle([int(i) for i in input().split()])
