import re
line = input()

print(len(re.findall(f'\\b{input()}\\b', line)))


'''My previous solution

import re

string, word = input(), input()

print(len(re.findall(fr'(\W?[^\w]{word}\W?[^\w])|(\b{word}\b)', string)))'''