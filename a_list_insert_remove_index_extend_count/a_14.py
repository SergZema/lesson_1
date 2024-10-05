"""
Задача 2. Вредоносное ПО
Гера решил попрактиковаться в программировании и захотел написать небольшой скрипт,
который после двух сообщений отправляет ещё одно на основе первых двух.
Пользователь вводит две строки. В каждой из них есть какое-то количество специальных символов ! и ?.
Напишите программу, которая считает количество этих символов отдельно в первой строке и отдельно во второй.
Если в первой строке их больше, чем во второй, то на экран выводится первая строчка, объединённая со второй,
а иначе — вторая с первой. При равном количестве символов в строках выводится «Ой».

Пример 1:
Первое сообщение: Привет!
Второе сообщение: Как дела? Что делаешь?

Третье сообщение: Как дела? Что делаешь? Привет!

Пример 2:
Первое сообщение: Хм!!
Второе сообщение: ?

Третье сообщение: Хм!!?

"""

first_messag = input('Первое сообщение:')
second_messag = input('Второе сообщение: ')
first_list = []
second_list = []
first_list.extend(first_messag)
second_list.extend(second_messag)
count_first = first_list.count('!') + first_list.count('?')
count_second = second_list.count('!') + second_list.count('?')
# for i in first_list:
#     if i == '!' or i == '?':
#         count_first += 1
# for i in second_list:
#     if i == '!' or i == '?':
#         count_second += 1
if count_first > count_second:
    print(first_messag + second_messag)
elif count_first < count_second:
    print(second_messag + first_messag)
else:
    print('Ой')
