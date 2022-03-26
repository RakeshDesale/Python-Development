# Using Function

# Solution:

def arrDiff(A,B,n):
    for i in range(n):
        print(A[i]-B[i],end=' ')

n = int(input())
A = [int(i) for i in input().split()]
arrDiff(A,[int(i) for i in input().split()],n)
