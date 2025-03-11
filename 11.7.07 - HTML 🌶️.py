import re, sys

for line in sys.stdin:
    match = re.search(r'href=\"(.+)\">(.+)</a', line)
    if match:
        print(match.group(1), match.group(2), sep=', ')


'''My previous code
import re, sys

for line in sys.stdin:
    regex = r'<a href=\"((https?:/)?/\w+\.?\w+\.?\w*/?.*)\">(.+)</a>'
    result = re.search(regex, line)
    if result:
        print(f'{result.group(1)}, {result.group(3)}')
        
'''