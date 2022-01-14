# Using Function

# Solution:

def checkBirthday(month,day):
    return 1 if (month=='july' and day==5) else 0

month=input()
day=int(input())
print(checkBirthday(month,day))
