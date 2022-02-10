# Without Using Function, Using List

# Solution:

s=input()
ch=input()
l=[]
for i in s:
    if i in "aeiou":
        l.append(ch)
    else:
        l.append(i)
print(''.join(l))
