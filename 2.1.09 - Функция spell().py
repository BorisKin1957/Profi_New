def spell(*args):
    alpha = [arg[0].lower() for arg in args]
    return {letter: len(word) for letter in alpha for word in sorted(args, key=len) if word[0].lower() == letter}



words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))

print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

print(spell())

words = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
print(spell(*words))

words = ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
print(spell(*words))

words = ['a']
print(spell(*words))

words = ['a', 'ab', 'abc', 'abcd', 'ба', 'аб', 'абвгдеЁёёЁЁжбБбБввВ', 'ёёё', 'Ёаaа']
print(spell(*words))

'''PREWIOSLY:

def spell(*args):
    new = [word.lower() for word in args]
    resalt = {}
    for word in new:
        key = word[0]
        k_filtered_new = filter(lambda i: i[0] == key, new) # список лишь из слов на букву key
        len_new = sorted(k_filtered_new, key=len)           # сортируем его по длине слова
        resalt[key] = resalt.get(key, len(len_new[-1]))     # длина последнего слова в списке - значение по ключу key
    return resalt'''