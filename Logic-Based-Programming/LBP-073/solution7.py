# Using Function

# Solution:

def zipCode(s):
    count=0
    for i in s:
        if i>='0' and i<='9':
            count+=1
    return count==5

print(str(zipCode(input())).lower())
