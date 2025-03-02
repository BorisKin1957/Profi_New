def triangle(n: int) -> str:
    if n > 0:
        print(n * '*')
        triangle(n - 1)


triangle(17)


'''My earlier version:

def triangle(n):
    if n > 0:
        print('*' * n)
        triangle(n - 1)'''