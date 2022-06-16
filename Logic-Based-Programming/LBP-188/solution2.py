# Using Function

# Solution:

def sum(n):
    sum = 0
    while n != 0:
        d = n % 10
        sum = sum + d
        n = n // 10
    return sum

n = int(input())
while(True):
    if n >= 0 and n <= 9:
        print(n)
        break
    else:
        n = sum(n)
