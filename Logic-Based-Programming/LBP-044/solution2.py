# Without Using Function

# Solution:

n=int(input())
l=[int(i) for i in input().split()]
sumeven=0
sumodd=0
for i in l:
    if i%2==0:
        sumeven+=i
    else:
        sumodd+=i
print(abs(sumeven-sumodd))
