# Using Function

# Solution:

def reward(s):
    return (s.count('A')>1 or s.count("LLL")!=0)
    
print("No" if reward(input()) else "Yes")
