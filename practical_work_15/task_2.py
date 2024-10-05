# Задание 2. Уникальное объединение списков
# Контекст
# Вы работаете в команде разработки программного обеспечения для компании, которая занимается обработкой и анализом данных.
# Ваша команда получает данные из различных источников, вам нужно объединить их в один отсортированный список для дальнейшей обработки.
# Однако источники данных возвращают отсортированные списки с возможными дубликатами, и ваша задача — создать программу,
# которая объединит эти списки в один отсортированный список без дубликатов.
# Задача
# Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный список без дубликатов.
# Пример:
# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
# merged = merge_sorted_lists(list1, list2)
# print(merged)
# Вывод в консоли:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Советы
# •	Учтите, что один список может быть короче другого.
# •	Проверьте ваше решение с различными тестовыми данными, включая случаи с пустыми списками,
# списками без дубликатов и списками с повторяющимися элементами.
# •	Требование отсутствия дубликатов значительно усложняет задачу. Убедитесь, что в вашем итоговом списке дубликатов не будет.

from random import randint

a = [randint(1, 10) for i in range(10)]
print(a)
b = [randint(1, 10) for i in range(10)]
print(b)
c = a + b
c.sort()
print(c)
n = []
for i in c:
    if i not in n:
        n.append((i))
print(n)


