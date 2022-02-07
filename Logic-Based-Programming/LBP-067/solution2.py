# Without Using Function

# Solution:

s=input()
flag=False
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        flag=True
        break
print(str(flag).lower())
