# Solution:

n=int(input())
flag=0
if n>=0:
    while n!=0:
        d=n%10
        if d==0:
            flag=1
            break
        n=n//10
    if flag==1:
        print("Yes")
    else:
        print("No")
else:
    pass
