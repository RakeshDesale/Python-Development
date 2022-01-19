# Using Function

# Solution:

def getSequenceSum(i,j,k):
    sum=0
    for a in range(i,j):
        sum=sum+a
    for a in range(j,k-1,-1):
        sum=sum+a
    return sum

print(getSequenceSum(int(input()),int(input()),int(input())))
