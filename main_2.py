def show_data(file_name):
    print("\nПП\t|ФИО\t|ТЕЛ\t")
    with open(file_name, "r",encoding="utf-8") as data:
        print(f"{data.read()}\n")

        
def edit_data(file_name):
    with open(file_name, "r",encoding="utf-8") as data:
        tel_book=data.read()
    print(f"{tel_book}\n")  

    index_del_data=int(input("Введите номер строки для изменения: ")) - 1

    tel_book_rows=tel_book.split("\n")

    edit_row=tel_book_rows[index_del_data]

    elements=edit_row.split("|")

    fio =input("Введите фамилию: ")
    tel=input("Введите номер телефона: ")

    num = elements[0]
    if len(fio)==0:
        fio=elements[1]
    if len(tel)==0:
        tel=elements[2]
    new_row=f"{num}\t|{fio}\t|{tel}\t"
    
    print (new_row)
    tel_book_rows[index_del_data]=new_row

    print(f"Запись - {edit_row}, изменена на - {new_row}\n")

    with open(file_name,"w",encoding="utf-8") as file:
        file.write("\n".join(tel_book_rows))

def add_data(file_name):
    with open(file_name,"r",encoding="utf-8") as file:
        tel_book=file.read().split("\n")
    num = len(tel_book)
    fio=input("Введите фамилию: ")
    tel=input("Введите номер телефона: ")
    with open(file_name,"a",encoding="utf-8") as data:
        data.write(f"{num}\t|{fio}\t|{tel}\t\n")
    print(f"Добавлена запись-{num}|{fio}|{tel}\n")

    

def del_data(file_name):
    with open(file_name, "r",encoding="utf-8") as data:
        tel_book=data.read()
    print(f"{tel_book}\n")  

    index_del_data=int(input("Введите номер строки для удаления: ")) - 1

    tel_book_rows=tel_book.split("\n")

    del_row=tel_book_rows[index_del_data]
    tel_book_rows.pop(index_del_data)
   
    print(f"Удалена запись {del_row}\n")

    with open(file_name,"w",encoding="utf-8") as file:
        file.write("\n".join(tel_book_rows))

def main():
    file_tel = "tel_book.txt"
    flag = -1
    # Создание файла
    with open(file_tel, "a", encoding="utf-8") as file_tel_creat:
        file_tel_creat.write("")

    while flag != 0:
        print("Выберите одно из действий:")
        print("1 - Вывести на экран")
        print("2 - Изменить данные")
        print("3 - Добавить данные")
        print("4 - Удалить данные")
        print("0 - Выход ")
        num_menu=int(input("Выберите пункт меню: "))
        if num_menu==1:
            show_data(file_tel)
            input("Для продолжения нажмите ENTER")
        elif num_menu==2:
            edit_data(file_tel)
            input("Для продолжения нажмите ENTER")
        elif num_menu==3:
            add_data(file_tel)
            input("Для продолжения нажмите ENTER")
        elif num_menu==4:
            del_data(file_tel)
            input("Для продолжения нажмите ENTER")
        else:
            flag=0
            print("Досвидания!")


main()
