def func(n=1, k=16):
    if n < 4:
        print((str(n) * k).center(16))
        func(n + 1, k - 4)
    print((str(n) * k).center(16))

func()


'''My earlier code:


def triangle(n, k=4):
    if k > 0:
        print((str(n - k + 1) * n * k).center(16))
        triangle(n, k - 1)
    if (n - 1 - k) > 0:
        print((str(n - 1 - k) * n * (k + 2)).center(16))


triangle(4)'''