# Using Function

# Solution:

def totalWt(W1,W2,W3,L1,L2):
    return W1+W2+W3 <= L1+L2

W1,W2,W3,L1,L2 = (int(i) for i in input().split())
print("Yes" if totalWt(W1,W2,W3,L1,L2) else "No")
