def func(lst, start, end):
    print(lst)
    if start == 0 or end == len(lst) - 1:
            result = lst[:start] + lst[start:end] + lst[end:]
    else:
        result = lst[:start] + lst[start:end][::-1] + lst[end:]
        print(lst[start:end][::-1])
    print(result)
    return result



n, X, Y, A, B = map(int, input().split())


lst = [str(i) for i in range(1, n + 1)]
#
# print(''.join(lst[:X - 1]), ''.join(lst[X - 1:Y][::-1]),
#       ''.join(lst[A - 1:B][::-1]), ''.join(lst[B:]), sep='')

lst = func(lst, 0, X - 1)
lst = func(lst, X - 1, Y)
#func(lst, Y, A - 1)
lst = func(lst, A - 1, B)
lst = func(lst, B, len(lst))

# print(''.join(lst[X - 1:Y][::-1]))
# print(''.join(lst[A - 1:B][::-1]))
# print(''.join(lst[B:]))


# result = []
# result.extend(lst[:X - 1])
# print(*result)
# result.extend(lst[X - 1:Y][::-1])
# print(*result)
# result.extend(lst[A - 1:B][::-1])
# print(*result)
# result.extend(lst[B:])


# print(*result)


'''Previosly, I used the following code:

l = input().split()
nums = [int(i) for i in l]
numbers = [i for i in range(1, nums[0] + 1)]
x, y, a, b = nums[1], nums[2], nums[3], nums[4]
numbers = numbers[:x - 1] + numbers[x - 1:y][::-1] + numbers[y:]
numbers = numbers[:a - 1] + numbers[a - 1:b][::-1] + numbers[b:]

print(*numbers)'''