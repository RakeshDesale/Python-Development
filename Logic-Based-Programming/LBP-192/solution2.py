# Without Using Function

# Solution:

n = int(input())
for i in range(2,n+1):
    sum = 0
    temp = i
    while temp != 0:
        d = temp % 10
        sum = sum + (d * d * d)
        temp = temp // 10
    if i == sum:
        print(i,end=' ')
