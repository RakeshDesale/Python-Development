# Using Function

# Solution:

def vowelCount(s):
    count=0
    for i in s:
        if i in "aeiou":
            count+=1
    return count
    
print(vowelCount(input()))
