# Using Regular Expression

# Solution:

import re
mail=re.fullmatch("[a-z]+[0-9|_]@gmail[.]com",input())
print("true" if mail!=None else "false")
