'''Дано логическое выражение, состоящее из переменных, а также операторов |, &, and или or.
Напишите программу, которая разбивает данную строку по указанным операторам.'''

import re

regex = re.compile(r' *(?:\||and|&|or) *')

print(*re.split(regex, input()), sep=', ')