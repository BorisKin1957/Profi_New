import re

line, chars = input(), input()
regex = f'\\w({chars})({chars})*\\w'
List_chars = re.findall(regex, line)

print(len([j for i in List_chars for j in i if j]))

'''My previous solution wos more better and more easy:

import re

string = input()
print(len(re.findall(fr'\B{input()}\B', string)))'''