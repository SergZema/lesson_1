n = int(input('Введите количество чисел в списке: '))

number = []

for _ in range(n):
    num = int(input('Введите число: '))
    number.append(num)

k = int(input('Введите делитель: '))
summ = 0
count = 0
for i in number:
    if i % 10 == 0:
        summ += count
        print('Индекс числа', i, 'равен', count)
    count +=1
print('Сумма индексов =', summ)