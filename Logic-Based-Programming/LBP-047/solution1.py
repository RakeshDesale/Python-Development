# Solution:

def oddEven(n):
    if n>0:
        sum=0
        while n!=0:
            sum+=n%10
            n=n//10
    else:
        pass
    return sum%2==0
  
print("Evenish" if(oddEven(int(input()))) else "Oddish")
