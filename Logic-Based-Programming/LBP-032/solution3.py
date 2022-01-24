# Using ASCII Values

# Solution:

str=input()
count=0
for i in str:
    ch=ord(i)
    if (ch>=97 and ch<=122) or (ch>=65 and ch<=90) or (ch>=48 and ch<=57):
        pass
    else:
        count+=1
print (count)
