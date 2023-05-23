# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите число:"))
tempNumber = number
number1 = 0
tmp1 = ""
while number > 0:
    tmp = number % 10
    tmp1 = str(tmp) + tmp1
    if len(str(number)) > 1:
        tmp1 = " + " + tmp1
    number = int(number/10)
    number1 = number1+tmp
print(f" {tempNumber}  ->  {number1}  ({tmp1})")
