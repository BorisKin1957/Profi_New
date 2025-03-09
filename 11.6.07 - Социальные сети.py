import sys, re

count = 0

for line in sys.stdin:
    if re.search(r'.*beegeek.*', line, re.IGNORECASE):
        count += 1
print(count)

'''My previous solution:

import sys, re

count = 0

for line in sys.stdin:
    if re.search(r'.*beegeek.*', line, re.IGNORECASE):
        count += 1

print(count)'''