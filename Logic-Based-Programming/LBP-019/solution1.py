# Solution:

n=int(input())
a=list()
if n>=0:
    while n!=0:
        d=n%2
        a.append(d)
        n=n//2
    
    for i in reversed(a):
        print(i,end='')

else:
    pass
