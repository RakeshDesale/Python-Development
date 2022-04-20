# Using Function

# Solution:

def mulPrevNext(L):
    print(L[1],end=' ')
    for i in range(1,n-1):
        print(L[i-1]*L[i+1],end=' ')
    print(L[n-2])

n = int(input())
mulPrevNext([int(i) for i in input().split()])
