# Using Function

# Solution:

def uncensoredStr(cs,cv):
    j=0
    for i in cs:
        if i=='*':
            print(cv[j],end='')
            j+=1
        else:
            print(i,end='')

cs=input()
uncensoredStr(cs,input())
