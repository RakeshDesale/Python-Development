# Without Using Function

# Solution:

s=input()
ch=input()
newstr=""
for i in s:
    if i in "aeiou":
        newstr = newstr + ch
    else:
        newstr = newstr + i
print(newstr)
