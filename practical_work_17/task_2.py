"""
Задание 2. Самое длинное слово
Что нужно сделать
Пользователь вводит строку, содержащую пробелы. Найдите в ней самое длинное слово, выведите его и его длину.
Если таких слов несколько, выведите первое.
Пример 1
Введите строку: я есть строка.
Самое длинное слово: «строка».
Длина этого слова: 6 символов.
Пример 2
Введите строку: а б.
Самое длинное слово: «а».
Длина этого слова: 1 символ.
Пример 3
Введите строку: б.
Самое длинное слово: «б».
Длина этого слова: 1 символ.
"""
text = input('Введите строку: ').split()
# lenn = 0                                   # первый вариант
# for i in text:
#     if lenn < len(i):
#         lenn = len(i)
#
# for i in text:
#     if len(i) == lenn:
#         print(i)
#         break
# print(lenn)

# word = sorted(text.split(), key=len)[-1]      # Второй вариант
# print(word, len(word))

# clone = [len(i) for i in text]                # Третий вариант
# biggest = text[clone.index(max(clone))]
#
# print('Самое длинное слово: {}'.format(biggest))
# print('Длина этого слова: {}'.format(len(biggest)))

mxs=(text[0])                                    # Четвертый вариант
for i in range(1,len(text)):
    if len(text[i])>len(mxs):mxs=text[i]
print(mxs,len(mxs))

