regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

Validatingphonenumbers.py 
from re import compile, match

n = int(input())
for _ in range(n):
    phone_number = input()
    condition = compile(r'^[7-9]\d{9}$')
    if bool(match(condition, phone_number)):
        print("YES")
    else:
        print("NO")
