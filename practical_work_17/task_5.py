"""
Задание 5. Пароль
Что нужно сделать
При регистрации на сайте, помимо логина, нужно придумать пароль. Этот пароль должен состоять минимум из восьми символов,
содержать хотя бы одну большую букву и не менее трёх цифр. Тогда он будет считаться надёжным.
Напишите программу, которая просит пользователя придумать пароль до тех пор, пока этот пароль не станет надёжным.
Должна использоваться латиница.
Пример
Придумайте пароль: qwerty.
Пароль ненадёжный. Попробуйте ещё раз.
Придумайте пароль: qwerty12.
Пароль ненадёжный. Попробуйте ещё раз.
Придумайте пароль: qwerty123.
Пароль ненадёжный. Попробуйте ещё раз.
Придумайте пароль: qWErty123.
Это надёжный пароль.
"""
'''
while True:
    pas = input('Придумайте пароль: ')
    l = len(pas)
    z = len(list(filter(lambda x : x.isupper(), pas)))
    num = len(list(filter(lambda  x : x.isdigit(), pas)))
    if (l>=8) and (z>=1) and(num>=1):
        print('Это надежный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
'''


while True: 
password = input('Придумайте пароль: ') 
length = len(password) 
capital_letters = len([letter for letter in password if letter.isupper()]) 
numbers = len([letter for letter in password if letter.isdigit()]) 
if (length >= 8) and (capital_letters >= 1) and (numbers >= 3): 
print('Это надежный пароль!') 
break 
else: 
print('Пароль ненадёжный. Попробуйте ещё раз.')


"""
while True:

password = input('\nПридумайте пароль: ')

if (sum(letter.isupper() for letter in password) < 1) \
or (sum(letter.isnumeric() for letter in password) < 3) \
or (len(password) < 8):

print('\nПароль ненадёжный. Попробуйте ещё раз.\n') \


else:
print('\nЭто надёжный пароль!')
break
"""

"""
def my_isupper(string): 
flag = False 
for i in string: 
if i.isupper(): 
flag = True 
return flag 


def is_three_digits(string): 
count = 0 
for i in string: 
if i.isdigit(): 
count += 1 
if count >= 3: 
return True 
return False 


while True: 
password = input('Придумайте пароль: ') 
if len(password) >= 8 and my_isupper(password) and is_three_digits(password): 
print('Это надёжный пароль!') 
break 
else: 
print('Пароль ненадёжный. Попробуйте ещё раз.')
"""