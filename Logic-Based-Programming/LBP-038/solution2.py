# Solution:

s=input()
count=0
if len(s)!=0:
    for i in s:
        if ((i>='A' and i<='Z') or (i>='a' and i<='z') or (i>='0' and i<='9') or (i==' ')):
            continue
        else:
            count+=1
    print (count)
else:
    pass
