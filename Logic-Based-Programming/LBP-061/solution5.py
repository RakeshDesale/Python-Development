# Using ASCII and Using Constraints

# Solution:

s=input()
if len(s)==2:
    if ((ord(s[0])>=97 and ord(s[0])<=104) and (ord(s[1])>=49 and ord(s[1])<=56)):
        x=ord(s[0])-96
        y=ord(s[1])
        print(str(x%2!=y%2).lower())
    else:
        pass
else:
    pass
