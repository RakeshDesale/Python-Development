# Using Function

# Optimized Solution:

def isPalindrome(n):
    rev = 0
    temp = n
    while n!=0:
        d = n%10
        rev = rev*10+d
        n = n//10
    return temp == rev

n = int(input())
print(sum([int(i) for i in input().split() if isPalindrome(int(i))]))
