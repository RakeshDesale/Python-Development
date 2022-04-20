# Without Using Function

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
for i in L:
    t = L.count(i)
    if(t==1):
        print(i)
