# Solution:

s=input()
counter=0
for i in s:
    if i>='0' and i<='9':
        counter+=1
print("true" if counter==5 else "false")
