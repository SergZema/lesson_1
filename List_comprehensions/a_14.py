"""
Задача 3. Удаление части
Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B).
Напишите программу, которая удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков
"""
import random
nums = [x for x in range(10)]
print(nums)
b = 1
a = 2
while b <= a:
    a = random.randint(1,9)
    b = random.randint(1, 9)
print(a)
print(b)

nums = nums[:a:] + nums[b::]
print(nums)