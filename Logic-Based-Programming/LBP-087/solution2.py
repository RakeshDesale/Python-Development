# Using Function

# Solution:

def balancedParenthesis(s):
    count=0
    for i in s:
        if i=='(':
            count+=1
        elif i==')':
            count-=1
    return count

print(balancedParenthesis(input()))
