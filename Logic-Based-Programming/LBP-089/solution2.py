# Using Function

# Solution:

def rotation(str1,str2):
    return str2 in str1+str1

str1=input()
print(str(rotation(str1,input())).lower())
