# Using ASCII Values

# Solution:

s=input()
count=0
if len(s)!=0:
    for i in s:
        if ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57) or (ord(i)==32)):
            continue
        else:
            count+=1
    print (count)
else:
    pass
