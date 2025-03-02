def print_digits(number:int)-> int:
    if number > 0:
        print_digits(number // 10)
        print(number % 10)

print_digits(12345)

'''My previous code:

def print_digits(n):
    if str(n):
        print(str(n)[0])
        print_digits(str(n)[1:])'''