n, leng_words = int(input()), {}
for i in range(n):
    words = input().split(', ')
    for word in words:
        leng_words[word] = leng_words.get(word, 0) + 1

result = sorted([key for key, value in leng_words.items() if value == n])

print(', '.join(result) if result else 'Сериал снять не удастся')

'''My previous version:

n = int(input())
lang_set = set(input().split(', '))
flag = True

for i in range(n - 1):
    lang_set &= set(input().split(', '))
    if lang_set:
        continue
    else:
        flag = False
        break

print(['Сериал снять не удастся', ', '.join(sorted(lang_set))][flag])'''