import re, sys

for line in sys.stdin:
    print(True if re.findall(r'\b_\d+[A-Za-z]*_?$', line) else False)

'''My previous solution:
from re import fullmatch
import sys

for line in sys.stdin:
    match = fullmatch('_\d+[A-Za-z]*_?', line.strip())
    if not match:
        print(False)
    else:
        print(True)
'''
