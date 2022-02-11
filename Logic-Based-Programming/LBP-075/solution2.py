# Without Using Function

# Solution:

st=input()
for i in range(len(st)):
    if st[i] in "aeiou":
        print(i)
        break
