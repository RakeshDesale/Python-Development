# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort()
low = 0
high = n-1
while(low <= high):
    print(L[low],L[high],end=' ')
    low += 1
    high -= 1
