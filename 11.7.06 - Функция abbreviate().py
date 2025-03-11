import re

def abbreviate(phrase):
    return ''.join(re.findall(fr'\b\w|\B[A-Z]', phrase)).upper()

print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))
print(abbreviate('gaveOver GameStarted happyEnd happyend'))


'''My previous solution

import re

def abbreviate(phrase):
    L = []
    new = re.findall(r'\b\w*[A-Z]|\b\w', phrase)
    for i in new:
        if len(i) > 1:
            L.append(i[0] + i[-1])
        else:
            L.append(i)
    return ''.join(L).upper()'''
