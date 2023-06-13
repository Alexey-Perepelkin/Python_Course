n = int(input()) #сколько можем проехать за день
m = int(input()) #сколько надо проехать
d = m/n%1
print (m/n)
print (f"остаток от деления {d}")
flag =d>0
print(f"результат flag {flag}")
d1 =1*(d>0)
print (f"добавление дробной части {d1}")
print(f"{int(m/n)+d1} дня")