''' Задание было изменено авторами
Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:

    состоит из 44, 55 или 66 символов
    состоит только из цифр (0−90−9)
    не содержит пробелов

Реализуйте функцию is_valid(), которая принимает один аргумент:'''


def is_valid(string: str):
    if 4 <= len(string) <= 6:
        return all(map(lambda x: (x.isdigit() and x != ' '), string ))
    return False

print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
print(is_valid('467'))
print(is_valid('4323423424467'))
print(is_valid('3 7 0'))
print(is_valid('0000'))
print(is_valid(''))
print(is_valid('aaaa'))

'''def is_valid(pin_cod):
    return 3 < len(pin_cod) < 7 and pin_cod.isdigit()'''