def dict_travel(nested_dict, prefix=''):
    for key, value in sorted(nested_dict.items()):
        if isinstance(value, dict):
            dict_travel(value, prefix + key + '.')
        else:
            print(*[prefix + key + ':', value])


my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
dict_travel(my_dict)


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)

data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)


'''My previous solution:

def dict_travel(all_dict):
    # возвращаем отсортированный и сформатированный словарь
    def travel(data):   
        L, d = {}, {}
        for key, value in data.items():
            if type(value) == dict:
                for kk, vv in value.items():
                    kk = str(key) + '.' + str(kk)
                    d.setdefault(kk, vv)

                L.update(travel(d))
            else:
                L.update({key: value})
        L = sorted(L.items(), key=lambda x: x[0])

        return L
    # Распечатываем словарь
    for i in travel(all_dict): # 
        print(f'{i[0]}: {i[1]}')'''