# Задание 3. Видеокарты
# Что нужно сделать
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий хранятся только числа,
# которые обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт.
# Самые старшие поколения разобрали за пару дней.
# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.
# Пример:
# Количество видеокарт: 5
# Видеокарта 1: 3070
# Видеокарта 2: 2060
# Видеокарта 3: 3090
# Видеокарта 4: 3070
# Видеокарта 5: 3090
#
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]


list_Vcards = []
num = int(input('Введите количество видеокарт: '))
for i in range(1, num + 1):
    name = int(input(f'Видеокарта {i}: '))
    list_Vcards.append(name)


maximum = list_Vcards[0]

for i in list_Vcards:

    if maximum < i:
        maximum = i

# print(maximum)
new_list_Vcards = []
for i in list_Vcards:
    if i != maximum:
        new_list_Vcards.append(i)

print('Старый список видеокарт: ', list_Vcards)
print('Новый список видеокарт: ', new_list_Vcards)