def is_palindrome(string: str):
    if len(string) < 2:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


print(is_palindrome('abcbe'))
print(is_palindrome('stepik'))

print(is_palindrome('123454321'))
print(is_palindrome('1234554321'))
print(is_palindrome('d'))

'''My previous solution:

def is_palindrome(string):
    if len(string) == 1 or string == '':
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False'''