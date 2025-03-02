def triangle(n: int) -> str:
    if n > 0:
        triangle(n - 1)
    print(n * '*')


triangle(17)


'''y earlier version:

def triangle(n, k=1):
    if n > 0:
        print('*' * k)
        k += 1
        triangle(n - 1, k)'''