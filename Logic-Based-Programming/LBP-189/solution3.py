# Using Function

# Solution:

def absDiff(n):
    return (abs(int(n) - int(n[::-1])))

print(absDiff(input()))
