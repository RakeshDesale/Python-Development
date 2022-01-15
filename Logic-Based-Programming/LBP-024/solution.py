# Solution:

x=int(input())
y=int(input())
sum=0
for i in range(x,y+1,1):
    if(i%2==0):
        sum=sum+i
    else:
        pass
print (sum)
