def get_pow(a, n):
    if n == 0:
        return 1
    return a * get_pow(a, n - 1)
    
print(get_pow(5, 2))

'''My previous code:

def get_pow(a, n):
    if n > 0:
        return a * get_pow(a, n - 1)
    return 1'''