# Without Using Function

# Optimized Solution:

n1=int(input())
n2=int(input())
s=0
for i in range(n1,n2+1):
    s=s+sum([int(j) for j in str(i)])
print(s)
