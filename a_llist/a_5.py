id_in = []
num = int(input('Сколько сотрудников на работе? '))
for _ in range(num):
    id = int(input('ID сотрудника: '))
    id_in.append(id)
id_search = int(input('Какой ID ищем?'))
flag = None
for id in id_in:
    if id == id_search:
        flag = True
    else:
      flag = False
if flag == True:
    print('Сотрудник с ID', id_search, 'на работе!')
else:
    print('Сотрудник с ID', id_search, 'не на работе!')