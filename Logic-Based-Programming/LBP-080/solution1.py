# Solution:

import re
def validHex(s):
    return re.fullmatch("#[A-Fa-f0-9]{6}",s)!=None

print(str(validHex(input())).lower())
