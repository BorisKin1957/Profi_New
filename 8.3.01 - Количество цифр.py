def get_len_number(number):
    if not number:
        return 0
    return 1 + get_len_number(number // 10)


print(get_len_number(int(input())))


'''My previous code 1:

def f(n, k=0):
    if str(n) == '':
        print(k)
    else:
        f(str(n)[1:], k + 1)


f(input())'''

'''My previous code 2:

def get_len_namber(number, lenght=0):
    if not number:
        print(lenght)
    else:
        lenght += 1
        get_len_namber(number // 10, lenght)

        
get_len_namber(int(input())))'''