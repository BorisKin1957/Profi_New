def choose_plural(number, words):
    n = int(str(number)[-1])
    if n == 1 and (number < 10 or 20 < number < 100):
        return f'{number} {words[0]}'
    elif 1 < n < 5 and number < 10 or (1 < n < 5 and str(number)[-2] != '1'):
        return f'{number} {words[1]}'
    return f'{number} {words[2]}'

print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))
print(choose_plural(2, ('пример', 'примера', 'примеров')))
print(choose_plural(111, ('пример', 'примера', 'примеров')))
print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))

print()

print(choose_plural(116, ('перец', 'перца', 'перцев')))

'''PREVIOSY:


def choose_plural(num, word_shit):
#    if str(num)[-1] == '1' and str(num)[-2] != '1':
    if str(num)[-1] == '1' and len(str(num)) == 1 or str(num)[-1] == '1' and str(num)[-2] != '1':
        result = f'{num} {word_shit[0]}'
    elif str(num)[-2:] in ['11', '12']:
        result = f'{num} {word_shit[2]}'
    elif str(num)[-1] in '234':
        result = f'{num} {word_shit[1]}'
    else:
        result = f'{num} {word_shit[2]}'

    return result'''