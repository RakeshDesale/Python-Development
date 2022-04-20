# Solution:

def uniqueNumber(L):
    for i in L:
        t = L.count(i)
        if(t==1):
            return i

n = int(input())
print(uniqueNumber([int(i) for i in input().split()]))
