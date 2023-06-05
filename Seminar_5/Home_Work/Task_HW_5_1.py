# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)
a = int(input("A = "))
b = int(input("B = "))
result = expt(a, b)
print(f"A = {a}; B = {b} -> {result} ")
