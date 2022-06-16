# Using Core Logic

# Solution:

n = int(input())
temp = n
rev = 0
while temp != 0:
    d = temp % 10
    rev = rev * 10 + d
    temp = temp //10
print(abs(n - rev))
