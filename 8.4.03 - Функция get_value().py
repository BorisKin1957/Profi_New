def get_value(nested_list, key):
    if key in nested_list:
        return nested_list[key]
    for value in nested_list.values():
        if isinstance(value, dict):
            result = get_value(value, key)
            if result:
                return result


data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))

data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))

'''My previous solution:

def get_value(data, key):
    if key in data:
        return data[key]

    for v in data.values():
        if type(v) == dict:
            value = get_value(v, key)
            if value is not None:
                return value'''

