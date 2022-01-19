# Using Function

# Solution:

def checkPrime(n):
    if n>1:
        flag=0
        for i in range(2,int(n/2)+1):
            if n%i==0:
                print("false")
                flag=1
                break
        if flag==0:
            print("true")
    else:
        pass

checkPrime(int(input()))
