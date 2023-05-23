# Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input("Введите число:"))
number1 = 0
count = 0
while number > 0:
    tmp = number % 10
    number = int(number/10)
    number1 = number1+tmp
    count = count+1
print(f"Сумма {count} значного числа = {number1}")