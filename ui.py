from logger import input_data, print_data, update_data, delete_data, copy_data

def interface():
    print("Добрый день! Вы попали на специальный бот справочник!")
    print("1 - запись данных")
    print("2 - вывод данных")
    print("3 - изменение данных")
    print("4 - удаление данных")
    print("5 - копирование данных")
    command = int(input('Введите число '))

    while command not in [1, 2, 3, 4, 5]:
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data()
    elif command == 5:
        copy_data()



















