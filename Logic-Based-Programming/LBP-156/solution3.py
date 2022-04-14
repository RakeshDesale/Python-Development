# Using Function

# Solution:

def indexChar(st,L,n):
    for i in range(n):
        print(st[L[i]].lower(),end='')

st = input()
n = int(input())
indexChar(st,[int(i) for i in input().split()],n)
