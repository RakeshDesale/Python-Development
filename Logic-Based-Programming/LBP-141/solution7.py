# Another Approach Using Function and Without Return Value

# Solution:

def rearrangeArr(L):
    L = sorted(L)
    low = 0
    high = n-1
    while(low <= high):
        print(L[low],L[high],end=' ')
        low += 1
        high -= 1

n = int(input())
rearrangeArr([int(i) for i in input().split()])
