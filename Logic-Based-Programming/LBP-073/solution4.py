# Using Core Logic:

# Solution:

s=input()
flag=0
if(len(s)==5):
    for i in s:
        if i>='0' and i<='9':
            continue
        else:
            flag=1
            break
else:
    flag=1
print("true" if flag==0 else "false")
