# Traditional Approach

# Solution:

s=input()
Acount=0
Bcount=0
Ccount=0
for i in s:
    if i=='A':
        Acount+=1
    elif i=='B':
        Bcount+=1
    else:
        Ccount+=1
print(Acount,Bcount,Ccount)
