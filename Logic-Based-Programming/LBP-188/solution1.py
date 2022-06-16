# Solution:

n = int(input())
while(True):
    if n >= 0 and n <= 9:
        print(n)
        break
    else:
        sum = 0
        while n != 0:
            d = n % 10
            sum = sum + d
            n = n // 10
        n = sum
