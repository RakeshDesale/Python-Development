# Solution:

n = int(input())
L = [int(i) for i in input().split()]
ele = int(input())
if ele in L:
    L.remove(ele)
    for i in L:
        print(i,end=' ')
else:
    print(-1)
