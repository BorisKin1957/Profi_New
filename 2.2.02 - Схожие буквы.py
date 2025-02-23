eng, rus = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
result = ['ru', 'mix', 'mix', 'en']
letters = [input() for _ in range(3)]
count = len(['en' for letter in letters if letter in eng])

print(result[count])


'''Previosly, I wrote a program that checks if the input is a letter in English or Russian.

l = [ord(input()) for _ in range(3)]

if sum(l) < 1000:
    print('en')
elif sum(l) > 3000:
    print('ru')
else:
    print('mix')'''