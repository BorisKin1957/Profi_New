'''Напишите программу, которая разбивает строку по символам точки, запятой и точки с запятой.'''

import re

regex = re.compile(r'[\.;,]')

for match in re.split(regex, input()):
    if match:
        print(match.strip(), end=' ')

