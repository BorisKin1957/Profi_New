n = int(input())

new = {str(a): sum(map(int, [int(i) for i in str(b)])) for a, b in enumerate(range(1, n + 1), start=1)}
new_sort = sorted(new.items())

res = {}
for k, v in new_sort:
    res.setdefault(str(v), []).append(int(k))

print(max([len(v) for v in res.values()]))

'''My previous code:

def sum_digit(num):
    return sum([int(i) for i in list(str(num))])

n = int(input())
num_list, result = [i for i in range(1, n + 1)], []

for i in range(n):
    l = []
    for num in num_list:
        x = sum_digit(num)
        if x == i:
            l.append(num)
    if l:
        result.append(l)

print(max([len(i) for i in result]))'''