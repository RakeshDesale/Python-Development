# Without Using Function

# Solution:

i=int(input())
j=int(input())
k=int(input())
sum=0
for a in range(i,j):
    sum=sum+a
for a in range(j,k-1,-1):
    sum=sum+a
print(sum)
