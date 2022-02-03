# Solution:

def swapString(str1,str2):
    str3=str1
    str1=str2
    str2=str3
    return str1+" "+str2

str1=input()
print(swapString(str1,input()))
