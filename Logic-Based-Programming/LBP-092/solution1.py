# Solution:

s=input()
ch=input()
count=1
if len(s)!=0:
    for i in s:
        if i==ch:
            print(count,end='')
            count+=1
        else:
            print(i,end='')
else:
    pass
