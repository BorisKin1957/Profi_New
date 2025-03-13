import re, keyword

regex = f"{'\\b|\\b'.join(keyword.kwlist)}"

print(re.sub(regex, '<kw>', input(), flags=re.I))


'''My previous solution:
import re
import keyword

def func_kw():
    list_kw = keyword.kwlist
    string = f'\\b{list_kw[0]}\\b'
    for word in list_kw[1:]:
        string += f'|\\b{word}\\b'
    return string


result = re.sub(func_kw(), '<kw>', input(), flags=re.I)
print(result)
'''