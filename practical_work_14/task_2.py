# Задание 2. Турнир
# Что нужно сделать
# Для двух дней соревнований по волейболу необходимо сформировать турнирную сетку из восьми человек.
# На первый день из списка участников решили выбрать каждого второго.
# Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар. Напишите программу,
# которая выводит элементы списка только с чётными индексами.
# Пример:
# Первый день: ['Артемий', 'Влад', 'Дима', 'Женя']
# Что оценивается
#

players = ['Артемий', "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
n = 0
new_list = []
for _ in range(4):
    new_list.append(players[n])
    n +=2
print(new_list)