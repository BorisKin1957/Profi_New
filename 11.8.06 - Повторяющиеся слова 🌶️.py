import re

result = input()

while re.search(r'\b(\w+)\W+\1\b', result):
    result = re.sub(r'\b(\w+)\W+\1', r'\1', result)

print(result)