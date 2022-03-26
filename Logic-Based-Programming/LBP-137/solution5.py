# Using Function and Return Value

# Solution:

def reverseArrEle(i):
    rev = 0
    while(i!=0):
        d = i%10
        rev = rev*10+d
        i = i//10
    return rev

n = int(input())
L = [int(i) for i in input().split()]
for i in L:
    print(reverseArrEle(i),end=' ')
