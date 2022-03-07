# Using List Sort (Reverse) Method

# Solution:

n = int(input())
L = [int(i) for i in input().split()]
L.sort(reverse=True)
print(L[n-1])
