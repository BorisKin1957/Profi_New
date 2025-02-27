def get_nic_name(nic_name: str) -> dict:
    '''# Функция get_nic_name принимает строку nic_name и возвращает словарь, где ключ - это имя,
    а значение - это число, которое следует за именем в строке nic_name.
    Если последний символ в строке nic_name не является цифрой,
    то функция возвращает словарь {nic_name: 0}
'''
    n = 0
    for i in range(len(nic_name)):
        if not nic_name[i].isdigit():
            n += 1
    if nic_name[-1].isdigit():
        return {nic_name[:n]: int(nic_name[n:])}
    return {nic_name: 0}


def get_free_namber(numbers: list) -> int:
    '''Функция get_free_namber принимает список чисел numbers и возвращает наименьшее число,
    которое отсутствует в списке. Если список пустой, то функция возвращает 0.
'''
    if numbers:
        numbers = sorted(numbers)
        for i in range(len(numbers)):
            if numbers[i] != i:
                return i
    return len(numbers)


base = {}
for i in range(int(input())):
    for name, number in get_nic_name(input()[:-12]).items():
        base.setdefault(name, []).append(number)
'''В этом цикле мы считываем строки из стандартного ввода, вызываем функцию get_nic_name для каждой строки 
и добавляем полученные значения в словарь base.
'''
for i in range(int(input())):
    new_name = input()
    if new_name in base:
        free_number = get_free_namber(base[new_name])
        base[new_name].append(free_number)
        if free_number != 0:
            print(f'{new_name}{free_number}@beegeek.bzz')
        else:
            print(f'{new_name}@beegeek.bzz')
    else:
        base.setdefault(new_name, [0])
        print(f'{new_name}@beegeek.bzz')
'''В этом цикле мы считываем строки из стандартного ввода, проверяем, есть ли имя в словаре base. 
Если имя есть, то мы вызываем функцию get_free_namber для списка чисел, связанных с этим именем, 
и добавляем полученное число в список. 
Если полученное число не равно 0, то мы выводим строку в формате '{new_name}{free_number}@beegeek.bzz', 
иначе - '{new_name}@beegeek.bzz'. 
Если имя не найдено в словаре, то мы добавляем его в словарь со значением [0] 
и выводим строку в формате '{new_name}@beegeek.bzz'.
'''


'''My previous code:

def name_num(s):
    s = s[:s.index('@')]
    num_s, alpha_s = '', ''
    for char in s:
        if char.isdigit():
            num_s += char
        elif char.isalpha() or char == '-':
            alpha_s += char
    if num_s:
            return [alpha_s, num_s]
    return [alpha_s, '0']

# база фамилий компании
beegeek = {}
# предельное значение однофамильцев
limit = 33

for mail in range(int(input())):
    s = input()
    name, num = name_num(s)[0], name_num(s)[1]
    beegeek[name] = beegeek.get(name, [str(i) for i in range(limit)])
    beegeek[name].remove(num)

for mail in range(int(input())):
    name = input()
    if name in beegeek:
        beegeek[name] = beegeek.get(name, [])
        if beegeek[name][0] == '0':
            print(f'{name}@beegeek.bzz')
        else:
            print(f'{name}{beegeek[name][0]}@beegeek.bzz')
        beegeek[name].remove(beegeek[name][0])
    else:
        beegeek[name] = beegeek.get(name, [str(i) for i in range(limit)])
        print(f'{name}@beegeek.bzz')

'''