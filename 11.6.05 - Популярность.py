import re
from sys import stdin
result = 0
for line in stdin:
    if line != '\n':
        if re.search(r'^beegeek', line) and re.search(r'beegeek$', line):
            result += 3
        elif re.search(r'beegeek$', line) or re.search(r'^beegeek', line):
            result += 2
        elif re.search(r'beegeek', line):
            result += 1
    else:
        break
print(result)

'''My previous solution was better

import sys
from re import search

count = 0

for line in sys.stdin:
    if search(r'beegeek.*beegeek', line):
        count += 3
    elif search(r'(^beegeek.*)|(.*beegeek$)', line):
        count += 2
    elif search(r'.+beegeek.+', line):
        count += 1

print(count)'''