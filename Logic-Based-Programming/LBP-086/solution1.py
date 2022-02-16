# Solution:

cs=input()
cv=input()
j=0
for i in cs:
    if i=='*':
        print(cv[j],end='')
        j+=1
    else:
        print(i,end='')
