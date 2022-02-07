# Without Using Function

# Solution:

s=input()
count1=0
count2=0
for i in s:
    if i=='x':
        count1+=1
    elif i=='o':
        count2+=1
print(str((count1==count2) or (count1==0 and count2==0)).lower())
