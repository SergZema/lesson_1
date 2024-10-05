user_name = input('Введите пользователя: ')
file_name = input('Введите имя файл: ')

# path = 'C:/{user}/docs/folder/{new_file}.txt'.format(
#     user = user_name,
#     new_file = file_name
# )

# path = 'C:/{0}/docs/folder/{1}.txt'.format(
#     user_name,
#     file_name
# )

path = f'C:/{user_name}/docs/folder/{file_name}.txt'

print('Путь к файлу:', path)