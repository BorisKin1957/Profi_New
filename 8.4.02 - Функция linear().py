def linear(old_list: list) -> list:
    new_list = []
    for i in old_list:
        if isinstance(i, int):
            new_list.append(i)
        elif isinstance(i, list):
            new_list.extend(linear(i))
    return new_list


print(linear([5, [3, 4, [2, [1, 7], 3], 4]]))

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

'''def linear(old_list: list) :
    return [i for i in old_list if isinstance(i, int)] + [j for i in old_list if isinstance(i, list) for j in linear(i)]'''

'''My previous code:

def linear(data):
    L = []
    for l in data:
        if type(l) == int:
            L.append(l)
        else:
            L += linear(l)
    return L
'''