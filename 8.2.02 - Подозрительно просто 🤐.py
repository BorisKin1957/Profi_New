def traffic(n=100):
    if n == 0:
        return
    traffic(n - 1)
    print(n)

traffic()


'''My previous version

def hundred(n):
    if n < 101:
        print(n)
        hundred(n + 1)


hundred(1)'''


