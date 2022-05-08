# Using Function

# Solution:

def nonRepeatChar(st):
    L = []
    for i in st:
        if st.count(i) == 1:
            L.append(i)
    return L[1]

print(nonRepeatChar(input()))
