# Using Function

# Solution:

def revDigit(n):
    rev = 0
    while n != 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    return rev

n = revDigit(int(input()))
while n != 0:
    d = n % 10
    if d % 2 == 0:
        print(d + 1,end='')
    else:
        print(d - 1,end='')
    n = n // 10
