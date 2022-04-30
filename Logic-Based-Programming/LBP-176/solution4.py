# Using Function and Using Core Logic

# Solution:

def gcdVal(num1,num2):
    gcd = 0
    for i in range(1,num1+1 and num2+1):
        if num1%i == 0 and num2%i == 0:
            gcd = i
    return gcd

num1,num2 = (int(i) for i in input().split())
print(gcdVal(num1,num2))
