# Solution:

size = int(input())
L = [int(i) for i in input().split()]
last = int(input())
if last>size:
    print(0)
else:
    for i in range(size-last,size):
        print(L[i],end=' ')
