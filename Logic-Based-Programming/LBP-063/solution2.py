# Without Using Function

# Solution:

str=input()
count=0
for i in str:
    if i in 'aeiou':
        count+=1
print(count)
