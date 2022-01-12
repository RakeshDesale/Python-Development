# Without Using String Function

# Solution:

n=int(input())
count=0
if n>0:
    while n!=0:
        n=n//10
        count+=1
    print (count)
else:
    pass
