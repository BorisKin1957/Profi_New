string, start, length = input(), 0, 0

new = string.replace(' 7', ' +7').replace(' 8', ' +8').replace('  ', ' ').split(', ')

for word in new:
    if ' +7' in word:
        start, length = word.index(' +7') + 2, 11
    if ' +8' in word:
        start, length = word.index(' +8') + 2, 12
    if start and length:
        result = word[start:start + 15]
        if result.replace('-', '').isdigit() and len(result.replace('-', '').strip()) == length:
            print(result)


'''My previous solution:

def is_phone_number(phone):
    groups = phone.split('-')
    tmp = list(map(lambda x: len(str(x)), groups))
    if groups[0] != '7' and groups[0] != '8' or (tmp != [1, 3, 3, 2, 2] and tmp != [1, 3, 4, 4]):
        return False
    chars = ''.join(groups)
    return all(c.isdigit() for c in chars)

def get_all_numbers(text):
    L = []
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            if '7' + chunk[1:] not in L and '8' + chunk[1:] not in L:
                L.append(chunk)
    return L

string = input()

print(*(i for i in get_all_numbers(string)), sep='\n')'''