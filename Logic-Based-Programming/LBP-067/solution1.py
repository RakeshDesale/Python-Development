# Solution:

def wordIdentical(s):
    flag=0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            flag=1
            break
    return flag==1

print(str(wordIdentical(input())).lower())
