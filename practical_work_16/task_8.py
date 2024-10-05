"""
Задание 8. Шифр Цезаря
Что нужно сделать
Юлий Цезарь использовал свой способ шифрования текста. Каждая буква заменялась на следующую по алфа-виту через K позиций по кругу.
Если взять русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать, буква А станет буквой Г, Б станет Д и так далее.
Пользователь вводит сообщение и значение сдвига. Напишите программу, которая изменит фразу при помощи шифра Цезаря.
Пример:
Введите сообщение: это питон.
Введите сдвиг: 3
Зашифрованное сообщение: ахс тлхср.
Что оценивается
•	Результат вычислений корректен.
•	Input содержит корректные приглашения для ввода.
•	Формат вывода соответствует примеру.
•	Алгоритм шифрования вынесен в отдельную функцию.
•	Переменные и функции имеют значимые имена, не только a, b, c, d.
"""



def cripto(message, shift):
    rus = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    alhabet = ''.join(rus)
    print(alhabet)
    message_cripto = ''
    for i in range(len(message)):
        letter = message[i]
        if letter == ' ':
            message_cripto += ' '
        else:
            i_litter = alhabet.index(letter)
            i_litter_cripto = i_litter + shift
            if i_litter_cripto < 31:
                message_cripto += alhabet[i_litter_cripto]
            else:
                i_litter_cripto = i_litter_cripto - 32
                message_cripto += alhabet[i_litter_cripto]
    return message_cripto

def cezar_chifr(messag, shift):
    eng = [chr(i) for i in range(ord('a'),ord('z') + 1)]
    n = eng[shift:] + eng[:shift]
    res = ''
    messag = list(messag.lower())
    for i in range(len(messag)):
        if messag[i] == ' ':
            res += ' '
        else:
            res += n[eng.index(messag[i])]
    res = list(res)
    res[0] = res[0].upper()
    return ''.join(res)

def ceaser_cipher(message, shift):
    rus = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    alhabet = ''.join(rus)
    char_list = [(alhabet[(alhabet.index(sym) + shift) % 32] if sym != ' ' else ' ') for sym in message]
    new_str = ''.join(char_list)

    return  new_str

message = input('Введите сообщение: ')
shift = int(input('Ведите сдвиг: '))
#print(cripto(message, shift))
#print(cezar_chifr(message, shift))
print(ceaser_cipher(message, shift))
