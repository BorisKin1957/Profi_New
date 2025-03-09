import re
from sys import stdin

for line in stdin:
    if line != '\n':
        if re.search(r'^Здравствуйте|^Доброе утро|^Добрый день|^Добрый вечер', line, re.IGNORECASE):
            print('True')
        else:
            print('False')
    else:
        break

'''My previous solution was better:

import re

if re.match(r'Здравствуйте|Доброе утро|Добрый день|Добрый вечер', input(), re.I):
    print(True)
else:
    print(False)
    '''