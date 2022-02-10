# Solution:

s=input()
counter=0
for i in s:
    if i.isdigit():
        counter+=1
print("true" if counter==5 else "false")
