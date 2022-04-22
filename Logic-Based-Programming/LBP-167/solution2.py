# Using Core Logic

# Solution:

n = int(input())
f = 1
count = 0
for i in range(1,n+1):
    f = f*i

while f!=0:
    if f%10 == 0:
        count += 1
    else:
        break
    f = f//10
print(count)
