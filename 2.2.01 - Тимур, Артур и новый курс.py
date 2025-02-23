d1, d2, d3 = [int(input()) for i in range(3)]

print(min(2 * d1 + 2 * d2, d1 + d2 + d3, 2 * d1 + 2 * d3, 2 * d2 + 2 * d3))

'''Previosly, we used the following code:

l = [int(input()) for i in range(3)]
print(min([2 * (l[0] + l[1]), 2 * (l[0] + l[2]), 2 * (l[1] + l[2]), sum(l)]))'''