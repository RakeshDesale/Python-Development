# Without Using Function

# Solution:

s = input()
sum = 0
for i in s:
    sum = sum + ord(i)-96
print("%.2f"%(sum/len(s)))
