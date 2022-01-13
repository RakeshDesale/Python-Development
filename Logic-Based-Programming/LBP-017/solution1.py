# Solution:

temp=n=int(input())
rev=0
if n>0:
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if temp==rev:
        print("Yes")
    else:
        print("No")
else:
    pass
