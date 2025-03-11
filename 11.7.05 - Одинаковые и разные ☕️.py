import re

word, line = input()[:-2], input()

print(len(re.findall(fr'\b{word}u?r\b', line, re.I)))


'''My previous solution

import re

word, string = input()[:-3], input()

print(len(re.findall(fr'\b{word}ou?r\b', string, re.IGNORECASE)))'''
