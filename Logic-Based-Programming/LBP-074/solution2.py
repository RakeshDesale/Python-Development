# Without Using Function

# Solution:

s=input()
n=len(s)
if(n%2==0):
    print(s[n//2-1],s[n//2],sep='')
else:
    print(s[n//2])
