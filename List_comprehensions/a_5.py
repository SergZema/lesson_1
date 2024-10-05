"""
Задача 3. Повышение цен
Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали,
что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.
Напишите программу, которая получает на вход список цен на товары (вещественные числа, список генерируется
также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.

Пример:
Цена на товар: 1.09
Цена на товар: 23.56
Цена на товар: 57.84
Цена на товар: 4.56
Цена на товар: 6.78
Повышение на первый год: 0
Повышение на второй год: 10
Сумма цен за каждый год: 93.83 93.83 103.21
"""

def input_price(i):
    return float(input(f'Цена на {i} товар: '))

def markup(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [input_price(i) for i in range(1,6)]
# print(prices_now)
first_percent = int(input('Повышение на первый год: '))
c=second_percent = int(input('Повышение на второй год: '))

prices_first = [markup(first_percent, i_price) for i_price in prices_now]
prices_second = [markup(second_percent, i_price) for i_price in prices_first]

print(prices_first)
print(prices_second)
print('Сумма цен за каждый год:', round(sum(prices_now), 2), round(sum(prices_first), 2), round(sum(prices_second), 2))

