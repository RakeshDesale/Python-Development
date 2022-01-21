# Another Way Without Using Function

# Solution:

n=int(input())
factors=0
for i in range(1,n+1):
    if(n%i==0):
        factors+=1
print(str(factors==2).lower())

# The above statement is written as str(factors==2).lower() - because, of we don't use like this, then we get the ans as "True" or "False" (first letter caps). So all test cases failed.
# Hence to convert that upper case letter into lower case, we use the str(arg).lower() method.
