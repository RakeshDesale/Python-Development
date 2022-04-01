# Solution:

def arrAvg(s):
    sum = 0
    for i in s:
        sum = sum + ord(i)-96
    return sum/len(s)


s = input()
print("%.2f"%(arrAvg(s)))
