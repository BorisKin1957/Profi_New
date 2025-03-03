def recursive_sum(numbers: list [int, list], result=0) -> int:
    if isinstance(numbers, list):
        for i in numbers:
            result += recursive_sum(i)
    else:
        result += numbers
    return result


print(recursive_sum([1, 2, [3, 4, [5, 6], 7], 8]))
print(recursive_sum([1, 2, 3, 4, 5]))
print(recursive_sum([1, 2, 3, 4, 5, [6, 7]]))
print(recursive_sum([1, 2, 3, 4, 5, [6, 7], [8, 9]]))

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))

'''My previous code:

def recursive_sum(data, L=[]):
    for l in data:
        if type(l) == int:
            L.append(l)
        else:
            recursive_sum(l)
    return sum(L)'''