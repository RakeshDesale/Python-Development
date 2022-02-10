# Using List

# Solution:

def midChar(s):
    l=[]
    n=len(s)
    if(n%2==0):
        l.append(s[n//2-1])
        l.append(s[n//2])
    else:
        l.append(s[n//2])
    return l

print(''.join(midChar(input())))
