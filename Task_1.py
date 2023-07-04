# Три друга взяли вещи в поход. Сформируйте словарь,
# где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# 1. Какие вещи взяли все три друга.
# 2. Какие вещи уникальны, есть только у одного друга.
# 3. Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует.
# Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {'Вася': ('палатка', 'спальник', 'аптечка'),
        'Петя': ('спальник', 'нож', 'веревка'),
        'Вова': ('топор', 'посуда', 'вода'),
        }

print(hike.values())

# 1. Какие вещи взяли все три друга.
things = []
for value in hike.values():
    things += value
print(f"1. Вещи, которые взяли все три друга: {set(things)}")

name_not = []
new_dict = {}
count = 0
for key, value in hike.items():
    name_not.append(key)
    new_dict[key] = []
    for j in value:
        for k in things:
            if k == j:
                count += 1
        if count == 1:
            new_dict[key] += [j]
        if count > 1:
            name_not.remove(key)
        count = 0

print(f"2. Уникальные вещи, есть только у одного друга. {new_dict}")
print("3. Вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует.", name_not)