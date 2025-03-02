def get_input():
    n = int(input())
    if n != 0:
        get_input()
    print(n)


get_input()


'''My previous code

import sys


def func(numbers, L=[]):
    for i in numbers:
        if i >= 0:
            L.append(numbers.pop(0))
        func(numbers)
    while L:
        print(L.pop(-1))


numbers = [int(i) for i in sys.stdin]

func(numbers)'''

