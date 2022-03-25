# Another Approach Using Function

# Solution:

def arrSum(L1,L2,n):
    for i in range(n):
        L1[i] = L1[i] + L2[i]
    return L1

n = int(input())
L1 = [int(i) for i in input().split()]
L2 = arrSum(L1,[int(i) for i in input().split()],n)
for i in L2:
    print(i,end=' ')
