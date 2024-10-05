
words_list = [['', 0], ['', 0], ['', 0]]

for i_num in range(3):
    #print(f'Введите {i_num+1} слово:', end=' ')
    word = input(f'Введите {i_num+1} слово: ')
    words_list[i_num][0] = word
text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index][0] == text:
            words_list[index][1] += 1
    text = input('Слово из текста: ')

print('n\Подсчет слов в тексте')
for index in range(3):
    print(words_list[index][0], ':', words_list[index][1])