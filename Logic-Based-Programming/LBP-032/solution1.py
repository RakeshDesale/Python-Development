# Solution:

str=input()
c=0
for i in str:
    if not i.isalnum():
        c+=1
print (c)
