def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)

traffic(5)
traffic(0)


'''My previous version

def traffic(n):
    while n > 0:
        print('Не парковаться')
        n -= 1'''