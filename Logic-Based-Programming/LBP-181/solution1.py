# Solution:

st = input()
L = []
for i in st:
    if st.count(i) == 1:
        L.append(i)
print(L[1])
