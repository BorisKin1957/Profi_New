
'''Традиционный подход к решению задачи с использованием рекурсии неэффективен
из-за повторного вычисления одних и тех же значений.
Для решения этой проблемы можно использовать мемоизацию,
сохраняя уже вычисленные значения в словаре cache, чтобы избежать повторных вычислений.

def func(n):
    if n == 0:
        return 0
    elif n < 4:
        return 1
    return func(n - 1) + func(n - 2) + func(n - 3)'''

'''Тот случай, когда якобы порочность использования изменяемого значения  
в качестве именованного параметра cache={1: 1, 2: 1, 3: 1} играет положительную роль. 
Это приводит к экономии машинного времени при последовательном вычислении числа из ряда Трибоначчи.'''


def tribonacci(n, cache={1: 1, 2: 1, 3: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return cache[n]

print(tribonacci(10))

print(tribonacci(300))
print(tribonacci(100))

'''My previous code:

def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}
    def trib_rec(n):
        result = cache.get(n)
        if result is None:
            result = trib_rec(n - 3) + trib_rec(n - 2) + trib_rec(n - 1)
            cache[n] = result
        return result
    return trib_rec(n)'''