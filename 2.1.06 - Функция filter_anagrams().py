def filter_anagrams(word: str, words: list[str]) -> list[str]:
    'возвращать список слов из списка words, которые представляют анаграмму слова word'
    return [i for i in words if sorted(i) == sorted(word)]


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
print(filter_anagrams('крона', ['кротко', 'укроп', 'норка']))
print(filter_anagrams('чулки', ['лучик', 'чутко', 'кочка']))
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))
word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
print(filter_anagrams(word, anagrams))

'''PREWIOSLY:

def filter_anagrams(word, word_list):
    return list(filter(lambda w: sorted(word) == sorted(w), word_list))
'''