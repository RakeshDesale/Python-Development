# Solution:

def maxDigit(n):
    m=0
    while n!=0:
        d=n%10
        if d>m:
            m=d
        n=n//10
    return m

n1=int(input())
n2=int(input())
n3=int(input())
if n1>=100 and n1<=999 and n2>=100 and n2<=999 and n3>=100 and n3<=999:
    w=min(n1%10,n2%10,n3%10)
    x=min((n1//10)%10,(n2//10)%10,(n3//10)%10)
    y=min((n1//100)%10,(n2//100)%10,(n3//100)%10)
    z=max(maxDigit(n1),maxDigit(n2),maxDigit(n3))
    print(z*1000+y*100+x*10+w)
else:
    pass
