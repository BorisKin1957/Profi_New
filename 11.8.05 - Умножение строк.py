import re

def get_simple(s: str) -> str:
    'Функция для получения строки n * string из линейной подстроки s вида n(string)'
    # регулярное выражение излишне функционально, но упрощать не стал, задолбавшись с иными косяками
    match = re.findall(r'([a-z]*)(\d+)\(([a-z]+)\)([a-z]*)', s)
    result = ''
    # Проходим по всем найденным вхождениям
    for i in match:
        # Добавляем к результату первую часть строки, умноженную на число, и вторую часть строки
        result += i[0] + int(i[1]) * i[2] + i[3]
    return result

s = input()

# Пока в строке есть символ ')', продолжаем обработку
while s.count(')'):
    # Используем регулярное выражение для поиска первого вхождения шаблона в строке s
    reg = re.search(r'(\b[^\)]*?)(\d+\([a-z]+\))(.*)', s)

    # Если первая группа не найдена, устанавливаем a равным пустой строке
    if not reg.group(1):
        a = ''
    else:
        a = reg.group(1)

    # Если вторая группа не найдена, устанавливаем b равным пустой строке
    if not reg.group(2):
        b = ''
    else:
        b = reg.group(2)

    # Если третья группа не найдена, устанавливаем c равным пустой строке
    if not reg.group(3):
        c = ''
    else:
        c = reg.group(3)

    # Обновляем строку s, заменяя найденное вхождение на результат обработки
    s = a + get_simple(b) + c

print(s)