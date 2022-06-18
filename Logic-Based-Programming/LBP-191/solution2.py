# Without Using Function

# Solution:

n = int(input())
sum = 0
if n >= 1 and n <= 26:
    print(chr(n + 64))
else:
    while n != 0:
        d = n % 10
        sum = sum + d
        n = n // 10
    print(chr(sum + 64))
