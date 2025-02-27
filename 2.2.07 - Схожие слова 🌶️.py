def index_of_nearest(word):
    result = [i for i in range(len(word)) if word[i].lower() in 'ауоыиэяюёе']
    return result


word_index = index_of_nearest(input())

for _ in range(int(input())):
    word = input()
    if index_of_nearest(word) == word_index:
        print(word)

'''My previous solution:

def fun(word):
    count = 0
    sum_ind = []
    for i in range(len(word)):
        if word[i] in 'ауоыиэяюёе':
            count += 1
            sum_ind.append(i)
    return {count: sum_ind}


model = fun(input())

for i in range(int(input())):
    s = input()
    if fun(s) == model:
        print(s)'''



