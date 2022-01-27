# Using Inbuilt Function

# Solution:

s=input()
count=0
if len(s)!=0:
    for i in s:
        if i.isalnum() or i.isspace():
            continue
        else:
            count+=1
    print(count)
else:
    pass
