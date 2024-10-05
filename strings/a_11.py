user_name = input('Введите пользователя: ')
file_name = input('Введите имя файл: ')

path = 'C:/{user}/docs/folder/{new_file}'.format(
    user = user_name,
    new_file = file_name
)

if path.endswith('.txt'):
    print('Путь к файлу:', path)
else:
    print('Ошибка: неверное расширение файла.')