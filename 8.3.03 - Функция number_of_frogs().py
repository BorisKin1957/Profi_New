def number_of_frogs(year, frogs=77):
    if year == 1:
        return frogs
    else:
        frogs -= 30
        return number_of_frogs(year - 1, frogs * 3)


print(number_of_frogs(7))


'''My previous code:

def number_of_frogs(year, total=77):
    if year == 1:
        return total
    else:
        return number_of_frogs(year - 1, 3 * (total - 30))'''