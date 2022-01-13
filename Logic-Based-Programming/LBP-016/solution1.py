# Solution:

n=int(input())
key=int(input())
count=0
while n!=0:
    d=n%10
    if d==key:
        count+=1
    n=n//10
print(count)
