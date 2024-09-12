"""
Задача 1. Матрица
Дан вот такой список со списками:
matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
Реализуйте программу, которая выводит элементы этого списка в виде привычной нам матрицы.

Результат работы программы:
1 2 3
4 5 6
7 8 9

"""


matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end = ' ')
#     print()

# for row in matrix:
#     print(' '.join(map(str, row)))

# S = 0  #Сумма всех чисел матрицы
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         S += matrix[i][j]
# print(S)