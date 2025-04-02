'''Напишите программу, которая удаляет все комментарии из Python кода'''


import re, sys

l = [line for line in sys.stdin]

s = re.sub(r'^ *#.*\n', r'', ''.join(l), flags=re.MULTILINE)
s = re.sub(r' *#.*\n', r'\n', s, flags=re.MULTILINE)
s = re.sub(r'\s*""".*?"""', r'', s, flags=re.DOTALL)

print(s)