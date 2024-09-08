def selection_sort(my_list):

    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


from random import randint

nums = [randint(0, 100) for i in range(10)] # Генерация списка чисел
print(nums)

selection_sort(nums)

print(nums)