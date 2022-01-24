# Solution:

str=input()
count=0
for i in str:
    if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9'):
        pass
    else:
        count+=1
print (count)
