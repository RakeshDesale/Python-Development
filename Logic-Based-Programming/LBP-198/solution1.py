# Solution:

n = int(input())
temp = n
rev = 0
while temp != 0:
    d = temp % 10
    rev = rev * 10 + d
    temp = temp // 10
n = rev
while n != 0:
    d = n % 10
    if d % 2 == 0:
        print(d + 1,end='')
    else:
        print(d - 1,end='')
    n = n // 10
