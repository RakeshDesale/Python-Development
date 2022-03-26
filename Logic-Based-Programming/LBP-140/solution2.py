# Another Approach

# Solution:

n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
RES = []
for i in range(n):
    RES.append(A[i]-B[i])
for i in RES:
    print(i,end=' ')
