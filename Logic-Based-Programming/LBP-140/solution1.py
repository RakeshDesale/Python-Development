# Solution:

n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
for i in range(n):
    print(A[i]-B[i],end=' ')
