# Using Function

# Solution:

def trueOrFalse(s):
    count1,count2,count3=0,0,0
    for i in s:
        if i in "qwertyuiop":
            count1+=1
        elif i in "asdfghjkl":
            count2+=1
        elif i in "zxcvbnm":
            count3+=1
    return (count1==len(s) or count2==len(s) or count3==len(s))

print("true" if (trueOrFalse(input())) else "false")
