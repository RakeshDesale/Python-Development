# Using Function

# Solution:

def replaceChar(s,ch):
    if len(s)!=0:
        count=1
        for i in s:
            if i==ch:
                print(count,end='')
                count+=1
            else:
                print(i,end='')
    else:
        pass

s=input()
replaceChar(s,input())
