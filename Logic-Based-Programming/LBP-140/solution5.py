# Another Approach Using Function

# Solution:

def arrDiff(A,B):
    return A-B

n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
for i in range(n):
    print(arrDiff(A[i],B[i]),end=' ')
