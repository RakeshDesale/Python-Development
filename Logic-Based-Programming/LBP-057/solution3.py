# Using Function

# Solution:

def strReversed(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
print(strReversed(input()))
