# Using Function

# Optimized Solution:

def revDigit(n):
    while n != 0:
        d = n % 10
        if d % 2 == 0:
            print(d + 1,end='')
        else:
            print(d - 1,end='')
        n = n // 10

revDigit(int(input()[::-1]))
