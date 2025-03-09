from re import search
import sys

for line in sys.stdin:
    match = search(r'\b(\w+)\1\b', line)
    if match:
        print(match.group(1) * 2)


'''My previous solution
import sys
from re import search

for line in sys.stdin:
    word = line.strip()
    if len(word) % 2 == 0:
        h = int(len(word) / 2)
        word = word[:h] + ',' + word[h:]
        m = search('(\w+),(\w+)', word)
        if m.group(1) == m.group(2):
            print(m.group(1)+ m.group(2))'''