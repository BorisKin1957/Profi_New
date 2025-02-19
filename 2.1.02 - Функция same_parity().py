def same_parity(lst):
    if lst and lst[0] % 2 == 0:
        return [num for num in lst if num % 2 == 0]
    return [num for num in lst if num % 2 != 0]

print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity([]))
print(same_parity([1, 3, 5, 7, 9]))
print(same_parity([1, 2, 4, 6, 8]))
print(same_parity([-1, 1248234832443, 8]))
print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))
print(same_parity([2]))
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))