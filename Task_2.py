# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7, 7]
print(list)

res = set()
for i in list:
    list_v2 = list.count(i)
    if list_v2 > 1:
        res.add(i)
print(res)
