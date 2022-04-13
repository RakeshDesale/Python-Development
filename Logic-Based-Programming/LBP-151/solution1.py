# Solution:

n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in range(0,n-1):
    sum = sum + abs(L[i] - L[i+1])
print(sum)
