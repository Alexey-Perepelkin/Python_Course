# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random
size_set_1=int(input("Введите размерность первого множества: "))
size_set_2=int(input("Введите ращмерность второго множества: "))


def SetOfNumbers(size,first_rand,end_rand):
    new_set=set()
    for i in range(size):
        n=random.randint(first_rand,end_rand)
        new_set.add(n)
    return new_set

def SetSorted(creatad_set):
        list_1=list(creatad_set)
        return sorted(list_1)           

set_1=set(SetOfNumbers(size_set_1,1,10))
print(set_1)
set_2=set(SetOfNumbers(size_set_2,1,10))
print(set_2)

new_set=set_1.intersection(set_2)

new_list=list(SetSorted(new_set))
print(*new_list)