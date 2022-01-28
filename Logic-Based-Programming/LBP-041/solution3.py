# Using Function

# Solution:

def generateOTP(n):
    prod=1
    while n!=0:
        d=n%10
        prod*=d
        n=n//10
    return prod

print(generateOTP(int(input())))
