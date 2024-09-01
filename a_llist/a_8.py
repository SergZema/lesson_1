point_list = []
n = int(input('Введите количество собак: '))
print()

for dog in range(n):
    point = int(input(f'Количество очков за сезон для {dog + 1} собаки: '))
    point_list.append(point)

print(f'Список очков собак с багом: {point_list}')
minimum = point_list[0]
maximum = point_list[0]

for point in point_list:
    if point < minimum:
        minimum = point

for point in point_list:
    if point > maximum:
        maximum = point

for dog in range(n):
    if point_list[dog] == maximum:
        point_list[dog] = minimum
    elif point_list[dog] == minimum:
        point_list[dog] = maximum

print(f'Исправленные список - {point_list} ')