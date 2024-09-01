text = input('Введите текст')
replace_symbol = input('Какой символ заменяем: ')
new_symbol = input('На какой символ заменяем: ')

text_list = list(text)
new_text_list = []
count = 0
for symbol in text_list:
    if symbol == replace_symbol:
        symbol = new_symbol
        count += 1
    new_text_list.append(symbol)

for i in new_text_list:
    print(i, end='')

print('\nКоличество замен -', count)