'''Реализуйте функцию multiple_split(), которая принимает два аргумента:

    string — строка
    delimiters — список строк

Функция должна разбивать строку string на подстроки, используя в качестве разделителей строки из списка delimiters,
и возвращать полученный результат в виде списка.

Примечание 1. Другими словами, функция multiple_split() должна работать аналогично строковому методу split(), за тем исключением,
что delimiters может содержать не единственный разделитель, а целый набор разделителей.'''


import re

def multiple_split(string, delimiters):
    regex = ''
    for delimiter in delimiters:
        regex += re.escape(delimiter) + '|'
    regex = regex[:-1]
    return re.split(regex, string)

print(multiple_split('beegeek-python.stepik', ['.', '-']))
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
print(multiple_split('stepik_python-dima*roma*jenya-timur__arthur', ['_', '*', '#', '@']))
print(multiple_split('stepik__python@dima*roma*jenya----timur###arthur###bee', ['----', '__', '*', '###', '@']))
print(multiple_split('stepik.python.regular.expressions.split', ['.']))
print(multiple_split('stepikpythonregularexpressionssplit', ['.']))
print(multiple_split('stepik.python,regular*expressions+split', ['.', ',', '*', '+']))
print(multiple_split('stepik python regular expressions split', [' ']))
print(multiple_split('ivan_ivanov@company.com', ['.', '@', '_']))
print(multiple_split('beegeek[python(stepik^test', ['[', '(', '^']))
print(multiple_split('“There/was+an*Old:Man-with;a.beard"', ['/', '*', '+', ':', '-', '.', ';']))
print(multiple_split('“There//was++an**Old::Man--with;;a..beard"', ['//', '**', '++', '::', '--', '..', ';;']))
print(multiple_split('Two@Owls@and@a@Hen', ['@', '*', '+', ':', '-', '.', ';']))
print(multiple_split('There"was/a"small/boy"of/Quebec', ['/', '"']))