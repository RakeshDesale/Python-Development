# Using Function

# Solution:

def isPalindrome(L):
    return sum([int(i) for i in L if i==i[::-1]])

n = int(input())
print(isPalindrome(i for i in input().split()))
