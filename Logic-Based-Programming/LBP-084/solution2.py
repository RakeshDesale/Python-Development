# Without Using Function

# Solution:

s1=input()
l=list(s1)
l.sort()
s2=''.join(l)
print("true" if s1==s2 else "false")
