# Задача 5. Песни
# Что нужно сделать
# Мы пишем приложение для удобного прослушивания музыки. У Вани есть список из девяти песен группы Depeche Mode.
# В информацию о каждом треке входит название и продолжительность с точностью до долей минут:
# violator_songs = [
# ['World in My Eyes', 4.86],
# ['Sweetest Perfection', 4.43],
# ['Personal Jesus', 4.56],
# ['Halo', 4.9],
# ['Waiting for the Night', 6.07],
# ['Enjoy the Silence', 4.20],
# ['Policy of Truth', 4.76],
# ['Blue Dress', 4.29],
# ['Clean', 5.83]
# ]
# Из этого списка Ваня хочет выбрать N песен и добавить их в особый плейлист с другими треками.
# При этом ему важно, сколько времени в сумме эти N песен будут звучать.
# Напишите программу, которая запрашивает у пользователя количество песен из списка и их названия,
# а на экран выводит общее время их звучания.
# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean
# Общее время звучания песен — 14,93 минуты

# def time_song(name_song):
#     j = 0
#     for i in violator_songs:
#         if name_song in i:
#             time_i = violator_songs[j][1]
#             break
#         j += 1
#     return time_i



violator_songs = [
                ['World in My Eyes', 4.86],
                ['Sweetest Perfection', 4.43],
                ['Personal Jesus', 4.56],
                ['Halo', 4.9],
                ['Waiting for the Night', 6.07],
                ['Enjoy the Silence', 4.20],
                ['Policy of Truth', 4.76],
                ['Blue Dress', 4.29],
                ['Clean', 5.83]
                ]
n = int(input('Сколько песен выбрать? '))
sum_time = 0
for i in range(1, n + 1):
    name_song = input(f'Введите название {i}-й песни: ')
    # time_song(name_song)
    j = 0
    for i in violator_songs:
        time_i = 0
        if name_song in i:
            time_i = violator_songs[j][1]
            break
        j += 1
    sum_time += time_i

print(round(sum_time, 2))

