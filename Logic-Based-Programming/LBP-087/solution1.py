# Solution:

s=input()
count=0
for i in s:
    if i=='(':
        count+=1
    elif i==')':
        count-=1
print(count)
