# Solution:

def midChar(s):
    n=len(s)
    if n%2==0:
        return (s[n//2-1],s[n//2])
    else:
        return s[n//2]

t=(midChar(input()))
for i in t:
    print(i,end='')
