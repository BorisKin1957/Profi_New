import re

word_without_sufix = input()[:-2].lower()
regex = f'\\b{word_without_sufix}[sz]e\\b'

print(len(re.findall(fr'{regex}', input().lower())))

'''My previous solution was better:

import re

word, string = input()[:-2], input()

print(len(re.findall(fr'\b{word}[zs]e\b', string, re.IGNORECASE)))'''