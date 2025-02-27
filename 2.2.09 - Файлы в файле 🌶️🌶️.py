def get_bites(unit: str, size: int) -> int:
    'преобразование числа в байты'
    match unit:
        case 'B':
            return int(size)
        case 'KB':
            return int(size) * 1024
        case 'MB':
            return int(size) * (1024 ** 2)
        case 'GB':
            return int(size) * (1024 ** 3)
        case 'TB':
            return int(size) * (1024 ** 4)
        case _:
            return 0
def get_summary(bytes: int) -> list[int, str]:
    'преобразование байт в удобный вид'
    if bytes == 0:
        return [0, 'B']
    elif bytes < 1024:
        return [bytes, 'B']
    elif bytes < 1024 ** 2:
        return [round(bytes / 1024), 'KB']
    elif bytes < 1024 ** 3:
        return [round(bytes / 1024 ** 2), 'MB']
    elif bytes < 1024 ** 4:
        return [round(bytes / 1024 ** 3), 'GB']
    elif bytes < 1024 ** 5:
        return [round(bytes / 1024 ** 4), 'TB']


with open('files.txt', 'r', encoding='utf-8') as file:
    all_lines = file.readlines()
    all_files = {}
    'отсортируем все расширения'
    set_ext_sorted = sorted(set(map(lambda x: (x.split()[0]).split('.')[-1], all_lines)))

    for ext in set_ext_sorted:
        all_files[ext] = [[], []]
        for line in all_lines:
            if line.split()[0].split('.')[-1] == ext:
                all_files[ext][0].append(line.split()[0])
                #print(line.split()[1], line.split()[2])
                all_files[ext][1].append(get_bites(line.split()[2], line.split()[1]))

    summary_for_ext = {}
    for key, value in all_files.items():
        summary_for_ext[key] = get_summary(sum(value[1]))

    for ext in set_ext_sorted:
        for file_name in sorted(all_files[ext][0]):
            print(file_name)
        print(f'----------\nSummary: {summary_for_ext[ext][0]} {summary_for_ext[ext][1]}\n')


'''My previous code:

# объявляем словарь: {<расширение>: [<имя файла 1>, <имя файла 2>, ...], <общий размер в КВ>}
file_base = {}
with open('files.txt') as file:
    for line in file.readlines():
        s = line.split()
        ext = s[0][s[0].index('.') + 1:]    # расширение
        name = s[0][:s[0].index('.')]       # имя файла
        size = int(s[1])                    # размер
        unit = s[2]                         # Kb, B, GB
        # размерность в kB
        if unit.lower() == 'b':
            size = round(size / 1024, 1)
        elif unit.lower() == 'mb':
            size = round(size * 1024)
        elif unit.lower() == 'gb':
            size = round(size * 1024 ** 2)
        # заполняем словарь
        if ext in file_base:
            file_base[ext][0].append(name)
            file_base[ext][1] += size
        else:
            file_base[ext] = file_base.get(ext, [[name], size])
# сортируем ключи, имена файлов, приводим размеры к норме, выводим на печать
for ext in sorted(file_base):
    l = sorted(file_base[ext][0])
    size = file_base[ext][1]
    if 1024 < size < 1024 ** 2:
        size = round(size / 1024)
        unit = 'MB'
    elif 1024 ** 2 < size < 1024 ** 3:
        size = round(size / 1024 ** 2)
        unit = 'GB'
    else:
        size = round(size)
        unit = 'KB'
    for name in l:
        print(f'{name}.{ext}')
    print('-' * 10)
    print(f'Summary: {size} {unit}\n')
'''
