"""
Задача 1. Шифр Цезаря 2
Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря.
Напомним, что в таком способе шифрования каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования.
Не используйте конкатенацию и сделайте так, чтобы текст был в одном регистре.
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

message = input('Введите сообщение: ').lower()
shift = int(input('Ведите сдвиг: '))
#print(cripto(message, shift))
#print(cezar_chifr(message, shift))
print(ceaser_cipher(message, shift))