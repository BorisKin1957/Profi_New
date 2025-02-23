def likes(names: list[str]) -> str:
    match len(names):
        case 0:
            return "Никто не оценил данную запись"
        case 1:
            return f"{names[0]} оценил(а) данную запись"
        case 2:
            return f"{names[0]} и {names[1]} оценили данную запись"
        case 3:
            return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
        case _:
            return f"{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись"
        
        
print(likes(['Дима', 'Алиса']))
print(likes(['Эндрю', 'Тоби', 'Том']))
print(likes([]))
print(likes(['Том']))
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))
print(likes(['Эндрю', 'Тоби', 'Том', 'Артур', 'Тимур']))
print(likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса']))
names = [str(i) * 3 for i in range(100)]
print(likes(names))

'''PREW:

def likes(name_list):
    if len(name_list) == 1:
        return f'{name_list[0]} оценил(а) данную запись'
    elif 0 < len(name_list) < 3:
        return f'{name_list[0]} и {name_list[1]} оценили данную запись'
    elif 0 < len(name_list) < 4:
        return f'{name_list[0]}, {name_list[1]} и {name_list[2]} оценили данную запись'
    elif 0 < len(name_list) > 3:
        return f'{name_list[0]}, {name_list[1]} и {len(name_list[2:])} других оценили данную запись'

    return f'Никто не оценил данную запись'''