

text = input('Введите строку: ')
num = int(input('Номер символа:'))
count = 0

text_list = list(text)
print('Символ слева - ', text[num-2])
print('Символ справа - ', text[num])

symbol = text[num-1]

if symbol == text[num]:
    count += 1
if symbol == text[num-2]:
    count += 1
print(count)
