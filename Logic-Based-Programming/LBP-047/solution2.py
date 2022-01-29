# Without Using Function

# Solution:

n=int(input())
sum=0
if n>0:
    while n!=0:
        sum+=n%10
        n=n//10
    print("Evenish" if sum%2==0 else "Oddish")
else:
    pass
