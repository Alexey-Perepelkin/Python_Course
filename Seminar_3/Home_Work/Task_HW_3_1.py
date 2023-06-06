# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X 
import random
count= 0
num_list=int(input("Введите размерность списка: "))
num_range = int(input("Искать в диапазоне от 1 до "))
num_search=int(input("Введите искомое число:"))
list_1 = list() 
for i in range(num_list): 
    n=random.randint(0,num_range)
    list_1.append(n)
for i in range(num_list):
    if list_1[i] == num_search:
        count+=1
print(*list_1)
print(f"Число {num_search} встречается {count} раз")