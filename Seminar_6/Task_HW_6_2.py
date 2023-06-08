# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list_1 = list()
for i in range(20):
    n = random.randint(-10, 10)
    list_1.append(n)

min_number = int(input())
max_number = int(input())
print(f"список {list_1}")
print("*********")
for i in range(len(list_1)):
    if min_number > max_number:
        min_number,max_number = max_number,min_number
    if min_number <= list_1[i] <= max_number:
        print(f"{min_number} <= {list_1[i]} <= {max_number} \t под индексом {i}")