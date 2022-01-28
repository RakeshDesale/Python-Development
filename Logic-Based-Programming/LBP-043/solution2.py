# Using Function

# Solution:

def discount(n):
    sumeven=0
    sumodd=0
    while n!=0:
        d=n%10
        if d%2==0:
            sumeven+=d
        else:
            sumodd+=d
        n=n//10
    return sumeven*sumodd

print(discount(int(input())))
