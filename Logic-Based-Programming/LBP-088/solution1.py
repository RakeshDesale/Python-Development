# Solution:

str=input()
count1,count2,count3=0,0,0
for i in str:
    if i in "qwertyuiop":
        count1+=1
    elif i in "asdfghjkl":
        count2+=1
    elif i in "zxcvbnm":
        count3+=1
print("true" if count1==len(str) or count2==len(str) or count3==len(str) else "false")
