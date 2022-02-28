# Another Approach Using Function

# Solution:

def isPalindrome(n):
    temp = n
    rev = 0
    while(n!=0):
        d = n%10
        rev = rev*10+d
        n = n//10
    return temp == rev
    
n = int(input())
L = [int(i) for i in input().split()]
sum = 0
for i in L:
    if isPalindrome(i):
        sum = sum + i
print(sum)
