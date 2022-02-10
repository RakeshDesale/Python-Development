# Using Function

# Solution:

def zipCode(s):
    flag=0
    if len(s)==5:
        for i in s:
            if i>='0' and i<='9':
                continue
            else:
                flag=1
                break
        return flag==0
    else:
        return flag

print("true" if(zipCode(input())) else "false")
