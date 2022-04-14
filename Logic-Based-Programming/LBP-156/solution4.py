# Another Approach Using Function

# Solution:

def indexChar(st,L,n):
    for i in range(len(st)):
        for j in L:
            if j == i:
                print(st[i].lower(),end='')

st = input()
n = int(input())
indexChar(st,[int(i) for i in input().split()],n)
