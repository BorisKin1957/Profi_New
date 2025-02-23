def index_of_nearest(numbers, num):
    if numbers:
        result = list(map(lambda x: abs(x - num), numbers))
        return result.index(min(result))
    return -1


          
print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
print(index_of_nearest([6, 100, 101, 2], 4))
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))
print(index_of_nearest([1, 14, 100, 65, 6], 5))
print(index_of_nearest([10, 164, 100, 265, 16], 8))
print(index_of_nearest([10, 99, 0, -12, 16], -9))
print(index_of_nearest([1, 1, 1, 1, 1], 1))

'''Previosly:
def index_of_nearest(numbers, num):
    if numbers:
        numbers.append(num)
        new = sorted(numbers[:])            # добавляем в список наше число и сортируем
        before = new[new.index(num) - 1]    # узнаем числа меньшее и большее нашего
        after = new[new.index(num) + 1]
        if abs(abs(num) - abs(before)) < abs(abs(after) - abs(num)): # вычисляем разность, по меньшей разности находим нужное нам число
            return numbers.index(before)
        if abs(abs(num) - abs(before)) == abs(abs(after) - abs(num)): # если разности равны, ищем меньше из 2-ч чисел
            return min([numbers.index(before), numbers.index(after)])

        return numbers.index(after)
    return -1'''

