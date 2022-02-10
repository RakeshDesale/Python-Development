# Using Function and Constraints

# Solution:

def zipCode(s):
    if(len(s)==5):
        count=0
        for i in s:
            if i>='0' and i<='9':
                count+=1
        return count==5
    else:
        return False

print(str(zipCode(input())).lower())
