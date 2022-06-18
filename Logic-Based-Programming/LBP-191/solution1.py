# Solution:

def sumOfDigits(n):
    sum = 0
    while n != 0:
        d = n % 10
        sum = sum + d
        n = n // 10
    return sum

n = int(input())
while True:
    if n >= 1 and n <= 26:
        print(chr(n + 64))
        break
    else:
        n = sumOfDigits(n)
