def replace_part_of_list(original, start, end):
    original[start - 1:end] = original[start - 1:end][::-1]
    return original

n, X, Y, A, B = map(int, input().split())

lst = [str(i) for i in range(1, n + 1)]
lst = replace_part_of_list(lst, X, Y)
lst = replace_part_of_list(lst, A, B)

print(' '.join(lst))

'''Previously, I used the following code:

l = input().split()
nums = [int(i) for i in l]
numbers = [i for i in range(1, nums[0] + 1)]
x, y, a, b = nums[1], nums[2], nums[3], nums[4]
numbers = numbers[:x - 1] + numbers[x - 1:y][::-1] + numbers[y:]
numbers = numbers[:a - 1] + numbers[a - 1:b][::-1] + numbers[b:]

print(*numbers)'''