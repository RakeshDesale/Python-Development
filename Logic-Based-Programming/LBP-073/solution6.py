# Using Function

# Optimized Solution:

def zipCode(s):
    return (len(s)==5 and s.isnumeric())

print(str(zipCode(input())).lower())
