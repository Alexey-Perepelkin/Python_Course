# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
# пользователь будет вводить каждое число на новой строке для задач 10, 12.


num = int(input('Введите число: '))
p = 1
while p < num:
    print(p)
    p = (2 * p)