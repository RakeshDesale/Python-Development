# Using Function

# Solution:

def consonentCount(s):
    count=0
    for i in s:
        if i not in "aeiou":
            count+=1
    return count

print(consonentCount(input()))
