# Without Using Third String Variable

# Solution:

def swapString(str1,str2):
    str1=str1+str2
    str2=str1[0:(len(str1)-len(str2))]
    str1=str1[len(str2):]
    return str1+" "+str2

str1=input()
print(swapString(str1,input()))
