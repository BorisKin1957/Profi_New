from re import search, fullmatch
from sys import stdin
geek, geek_in, geek_out = [], 0, 0
for line in stdin:
    if line == "\n":
        break
    geek.append(line.lstrip().rstrip())

print(geek)
for item in geek:
    for word in item.split():
        match = fullmatch(r'(\bgeek\b)', word)
        if match:
            geek_out += 1
for item in geek:
    for word in item.split():
        match = fullmatch(r'geek', word)
        if match:
            geek_in += 1
print(geek_in)
print(geek_out)

'''My previous solution:

import sys
from re import search

count_bee, count_geek = 0, 0

for line in sys.stdin:
    match1 = search(r'(.*bee.*).*\1', line)
    match2 = search(r'\bgeek\b', line)
    if match1:
        count_bee += 1
    if match2:
        count_geek += 1

print(count_bee, count_geek, sep='\n')'''