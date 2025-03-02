def is_power(number, result=True):
    if number % 2 and number != 1:
        result = False
    elif number > 1 and result:
        return is_power(number / 2)
    return result




#print(is_power(256))
print(is_power(100))

'''My previous code:

def is_power(number):
    if number == 1:
        return True
    elif 0 < number < 2:
        return False
    else:
        return is_power(number / 2)
'''