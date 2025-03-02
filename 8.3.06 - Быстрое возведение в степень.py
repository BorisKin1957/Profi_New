def get_fast_pow(a, n):
    if n == 0:
         return 1
    else:
        if n % 2 == 0:
            result = get_fast_pow(a * a, n / 2)
        else:
            result = a * get_fast_pow(a, n - 1)
        return result



print(get_fast_pow(2, 100))

'''My previous code:
def get_fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        result = pow(a * a, n // 2)
    else:
        result = a * get_fast_pow(a, n - 1)
    return result
'''