# Using Function

# Solution:

def arrSum(L1,L2,n):
    for i in range(n):
        print(L1[i]+L2[i],end=' ')

n = int(input())
L1 = [int(i) for i in input().split()]
arrSum(L1,[int(i) for i in input().split()],n)
