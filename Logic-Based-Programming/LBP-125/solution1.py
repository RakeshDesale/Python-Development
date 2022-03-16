# Solution:

n = int(input())
L = [int(i) for i in input().split()]
oldele = int(input())
newele = int(input())
for i in range(0,n):
    if L[i]==oldele:
        L[i]=newele
for i in L:
    print(i,end=' ')
