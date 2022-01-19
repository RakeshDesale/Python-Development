# Without Using Function

# Solution:

n=int(input())
flag=0
if n>1:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print("false")
            flag=1
            break
    if flag==0:
        print("true");
else:
    pass
