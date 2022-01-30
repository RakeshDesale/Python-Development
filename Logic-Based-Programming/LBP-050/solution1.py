# Solution:

def sumOfDigits(n):
    sum=0
    while n!=0:
        sum=sum+n%10
        n=n//10
    return sum

n1=int(input())
n2=int(input())
sum=0
for i in range(n1,n2+1):
    sum=sum+sumOfDigits(i)
print(sum)
