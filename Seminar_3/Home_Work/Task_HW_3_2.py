# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

num_list = int(input("Введите размерность списка: "))
num_range = int(input("от 0 до  "))
num_search = int(input("Введите число для сравнения: "))


list_1 = list()
for i in range(num_list):
    n = random.randint(-20, num_range)
    list_1.append(n)
   # list_1.append(int(input()))
print(*list_1)

max_num = -float('inf')
min_num = float('inf')

difference_min = float('inf')
differenc_max = -float('inf')
for i in range(num_list):
    if list_1[i] != num_search:

        if list_1[i] > num_search:
            a = list_1[i]-num_search

            if a < difference_min:
                difference_min = a
                max_num = list_1[i]

        elif list_1[i] < num_search:
            b = list_1[i]-num_search

            if b > differenc_max:
                differenc_max = b
                min_num = list_1[i]

print(
    f"Близкое в большую сторону для числа {num_search} -> {max_num}")
print(
    f"Близкое в меньшую сторону сторону для числа {num_search} -> {min_num}")
