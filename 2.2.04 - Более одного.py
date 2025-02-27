numers = [int(num) for num in input().split()]
res = {num: numers.count(num) for num in set(numers)}

print(*(key for key, value in res.items() if value > 1))

'''My previously code:

numbers = [int(i) for i in input().split()]
print(*sorted(set(filter(lambda num: numbers.count(num) > 1, numbers))))'''