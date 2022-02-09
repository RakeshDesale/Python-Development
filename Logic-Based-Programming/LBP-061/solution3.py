# Using Constraints

# Solution:

s=input()
if len(s)==2:
    if ((s[0]>='a' and s[0]<='h') and (s[1]>='1' and s[1]<='8')):
        x=ord(s[0])-96
        y=ord(s[1])
        print(str(x%2!=y%2).lower())
    else:
        pass
else:
    pass
