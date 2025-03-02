def get_new_number(number):
    print(number)
    if number <= 0:
        return
    else:
        get_new_number(number - 5)
    print(number)


get_new_number(int(input()))


'''My previous code:

def minus_5(n):
    if n <= 0:
        print(n)
        return
    else:
        print(n)
        minus_5(n - 5)
    print(n)


minus_5(int(input()))
'''