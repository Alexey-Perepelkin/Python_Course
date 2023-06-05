# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии. 

def exponent(a, b):
    while b > 1:
        a*=a
        b-=1
        q = exponent(a,b)
    return a
print(exponent(2, 3))