# Using String replace() Method Without Using Function

# Solution:

s=input()
ch=input()
for i in "aeiou":
    s=s.replace(i,ch)
print(s)
