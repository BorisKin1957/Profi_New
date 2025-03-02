
def recursive_sum(a, b):
    if a > b:
        a, b = b, a
    if a < 999:
        if a == 0:
            return b
        return 1 + recursive_sum(a - 1, b)
    else:
        return ('Для больших чисел '
                'рекурсия с данными условиями задачи работает только тогда, '
                'когда одно из сомножителей меньше 999.')


print(recursive_sum(0, 0))


print(recursive_sum(1000000000000000, 998))


print(recursive_sum(1000000000000000, 999))
print(recursive_sum(998, 1000000000000000))



'''My earlier code:

def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)
    
Этот код порочен тем, что ограничен занчением b = 999, т.к. достигает максимальной глубины рекурсии.
Поэтому, для начала, нужно из а и b взять минимум, и уже из него вычитать 1, 
а затем, прибавить к нему результат рекурсии.'''