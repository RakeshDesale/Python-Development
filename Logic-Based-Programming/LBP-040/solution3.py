# Using Function

# Solution:

def revint(n):
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev

print(revint(int(input())))
