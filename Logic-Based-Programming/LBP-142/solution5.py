# Using Function and Return Value, Without Creating Array (List)

# Solution:

def multipleArr(m,i):
    return m*i

m = int(input())
n = int(input())
for i in range(1,n+1):
    print(multipleArr(m,i),end=' ')
