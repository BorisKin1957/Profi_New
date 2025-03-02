def to_binary(number: int) -> str:
    if number < 2:
        return str(number)
    return to_binary(number // 2) + str(number % 2)


print(to_binary(1023))
print(to_binary(1024))
print(to_binary(0))

'''My previous solution:

def to_binary(n, s='', i=0):
    if n > 0:
        s += str(n % 2)
        i += 1
        return to_binary(n // 2, s, i)

    else:
        if i == 0:
            return 0
        else:
            return s[::-1]
'''