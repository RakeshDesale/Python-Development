# Using Regular Expression and Without Using Function

# Solution:

import re
print("true" if re.fullmatch("#[A-F0-9a-f]{6}",input())!=None else "false")
