def get_sum_digits(number: int) -> int:
    'Сумма цифр числа'
    if not number:
        return 0
    return number % 10 + get_sum_digits(number // 10)


print(get_sum_digits(int(input())))


'''My previous code:

def f(n=input(), k=0):
    if str(n) == '':
        print(k)
    else:
        f(str(n)[1:], k + int(str(n)[0]))


f()'''