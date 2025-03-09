from re import search
import sys

phone_pattern = r'(\d{1,3})-(\d{1,3})-(\d{4,10})|(\d{1,3}) (\d{1,3}) (\d{4,10})'

while True:
    try:
        line = input()
        if search(phone_pattern, line):
            match = search(phone_pattern, line)
            if '-' in match.group(0):
                country = match.group(1)
                city = match.group(2)
                number = match.group(3)
            else:
                country = match.group(4)
                city = match.group(5)
                number = match.group(6)
            print(f'Код страны: {country}, Код города: {city}, Номер: {number}')
    except EOFError:
        break

'''My previous solution

Не верен, так как противоречит условию: оба вида разделителя в одном номере присутствовать не могут.:

from re import search
import sys

for line in sys.stdin:
    match = search('(\w{1,3})[- ](\w{1,3})[- ](\w{4,10})', line.strip('\n'))
    print(f'Код страны: {match.group(1)}, Код города: {match.group(2)}, Номер: {match.group(3)}')'''

