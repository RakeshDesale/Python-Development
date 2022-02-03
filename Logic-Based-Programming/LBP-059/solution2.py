# Using Function

# Solution:

def isAnagram(a,b):
    return sorted(a)==sorted(b)

a=input()
print("true" if(isAnagram(a,input())) else "false")
