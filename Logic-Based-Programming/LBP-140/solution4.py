# Using Function and Return Value

# Solution:

def arrDiff(A,B,n):
    for i in range(n):
        A[i] = A[i]-B[i]
    return A

n = int(input())
A = [int(i) for i in input().split()]
B = arrDiff(A,[int(i) for i in input().split()],n)
for i in B:
    print(i,end=' ')
