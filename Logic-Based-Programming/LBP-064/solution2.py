# Without Using Function

# Solution:

str=input()
count1=0
count2=0
for i in str:
    if i=='x':
        count1+=1
    elif i=='o':
        count2+=1
if (count1==count2) or (count1==0 and count2==0):
    print("true")
else:
    print("false")
