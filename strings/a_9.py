"""
Задача 1. Улучшенная лингвистика 2
Усовершенствуйте старую программу:
У нас есть список из трёх слов, которые вводит пользователь. Затем вводится сам текст произведения,
который вводится уже в одну строку. Напишите программу, которая посчитает,
сколько раз слова пользователя встречаются в тексте.
"""
# words_list = input('Введите слова для поиска в тексте через пробел: ').split()
# text = input('Введите текст:').split()
#
# for word in words_list:
#     count = 0
#     for text_words in text:
#         if text_words == word:
#             count += 1
#     print(f"Слово '{word}' встречается {count} раза.")

words,text = [input(f'Введите слово номер {i+1}:') for i in range(3)],input('Введите текст для поиска:').split()
for word in words:
    print(f'слово {word} встречается в тексте {text.count(word)} раз')