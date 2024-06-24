from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формета записать данные\n\n"
    f" 1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f" 2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    if var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)



def update_data():
    print("В каком файле внести изменения?")
    print("1 - Первый файл")
    print("2 - Второй файл")
    file_number = int(input('Введите число '))

    while file_number != 1 and file_number != 2:
        print("Неправильный ввод")
        file_number = int(input('Введите число '))

    if file_number == 1:
        file_name = 'data_first_variant.csv'
    else:
        file_name = 'data_second_variant.csv'

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Доступные записи:')
    for i, line in enumerate(data):
        if line != '\n':
            print(f'{i+1}. {line.strip()}')

    record_number = int(input('Введите номер записи, которую вы хотите изменить: '))

    if record_number < 1 or record_number > len(data) or data[record_number-1] == '\n':
        print('Неправильный номер записи')
        return

    new_data = input('Введите новые данные для записи: ')

    data[record_number-1] = new_data + '\n'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)

    print('Данные успешно изменены')


def delete_data():
    print("Из какого файла удалить запись?")
    print("1 - Первый файл")
    print("2 - Второй файл")
    file_number = int(input('Введите число '))

    while file_number != 1 and file_number != 2:
        print("Неправильный ввод")
        file_number = int(input('Введите число '))

    if file_number == 1:
        file_name = 'data_first_variant.csv'
    else:
        file_name = 'data_second_variant.csv'

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()

    print('Доступные записи:')
    for i, line in enumerate(data):
        if line != '\n':
            print(f'{i+1}. {line.strip()}')

    record_number = int(input('Введите номер записи, которую вы хотите удалить: '))

    if record_number < 1 or record_number > len(data) or data[record_number-1] == '\n':
        print('Неправильный номер записи')
        return

    data.pop(record_number-1)

    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)

    print('Запись успешно удалена')