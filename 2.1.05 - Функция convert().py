def convert(string):
    big = len(list(filter(lambda x: x.isupper(), string)))
    small = len(list(filter(lambda x: x.islower(), string)))
    return string.upper() if big > small else string.lower()


print(convert('BEEgeek'))
print(convert('pytHON'))
print(convert('pi31415!'))
print(convert('ABCDEF'))
print(convert('abcdef'))
print(convert('12345!?'))
print(convert('PI31415!'))
print(convert('ABCdef'))
print(convert('ABCdef123'))
print(convert('AbCdEf12345'))
print(convert('dEfAbC'))
