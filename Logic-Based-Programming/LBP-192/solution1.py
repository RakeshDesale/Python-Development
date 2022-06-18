# Solution:

def sum(n):
    sum = 0
    while n != 0:
        d = n % 10
        sum = sum + (d * d * d)
        n = n // 10
    return sum

n = int(input())
for i in range(2,n+1):
    if i == sum(i):
        print(i,end=' ')
