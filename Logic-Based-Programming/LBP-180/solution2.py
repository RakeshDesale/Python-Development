# Using Function

# Solution:

def parityCheck(n):
    return bin(n)[2::].count("1")%2==0

print("even" if parityCheck(int(input())) else "odd")
