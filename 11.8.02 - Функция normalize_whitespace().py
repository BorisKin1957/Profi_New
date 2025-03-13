import re

def normalize_whitespace(text):
    """Возвращает строку text, в которой все серии пробелов заменены на один пробел.
    Пробелы в начале и конце строки убираются."""
    return re.sub(r'\s+', ' ', text.strip())
    #return ' '.join([i.group() for i in re.finditer(r'[^\s]+', text)])
    #return ' '.join(re.findall(r'[^\s]+', text))

print(normalize_whitespace('AAAA                A                AAAA'))
print(normalize_whitespace('Тут нет лишних пробелов'))
print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
print(normalize_whitespace('K L  L    O    I!  !  I OP    PPPppdj O   P'))
print(normalize_whitespace('               '))
print(normalize_whitespace('aaaaaaaaaaaaaaaaaaaaaaaaaa'))
print(normalize_whitespace('Раз два  три   четыре    пять      шесть      '))
print(normalize_whitespace('      Шесть-----пять    четыре***три  два+один'))
print(normalize_whitespace('1 9  2  8   3   7    6    5'))
print(normalize_whitespace('Проб.елов,нетв-этом:очень\длинно*мслове'))
print(normalize_whitespace(''))
print(normalize_whitespace(' '))
print(normalize_whitespace('There are no unnecessary gaps.'))
print(normalize_whitespace('. ,  ;   :    "     (       )      '))
print(normalize_whitespace('111111111111 2222222222222 333333333333'))


'''My previous code:
import re

def normalize_whitespace(text):
    result = re.sub(r'\s+', r' ', text)

    return result
'''