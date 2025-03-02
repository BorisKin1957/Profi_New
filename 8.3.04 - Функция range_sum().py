def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    else:
        return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))


'''My previous code:

def range_sum(numbers, start, end, result=0):
    if start > end:
        return result
    return range_sum(numbers, start + 1, end, result + numbers[start])'''