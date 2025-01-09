import csv


def read():
    """чтение файла"""
    try:
        file_read = open('directory_enquiries.csv', 'r', encoding='UTF-8')
        file_reader = csv.reader(file_read, dialect='excel', delimiter=',')
        return file_reader
    except FileNotFoundError:
        return print('Скорее всего файла-справочника не существует \n')


def show_all():
    """Отображение всего содержимого справочника"""
    file = read()
    for line in file:
        if len(line) == 0:
            print('Файл пуст \n')
        else:
            print(line[1:])


def add_new():
    """добавить новый контакт в справочник"""
    file = read()
    pers_count = sum(1 for row in file)
    with open('directory_enquiries.csv', 'a', encoding='UTF-8') as file:
        new_pers = str(pers_count)
        file.writelines([new_pers, ','])
        new_pers = input('Введите Имя')
        new_pers += input('Введите номер')
        new_pers += input('Введите комментарий к персонажу')
        file.write(','.join(new_pers))
        file.writelines('\n')


def search():
    """Поиск информации в справочнике"""
    file = read()
    search_mode = input('Хотите поиск по полям, жмите 1, \nЕсли общий, то жмакайте 2')
    if search_mode in ('1', 1):
        print('По какому полю хотите найти?')
        search_column = input('1 - ID персонажа, 2 - Имя персонажа, 3 - Номер телефона, 4 - Внезапно Комментарий')
        if search_column in [1, 2, 3, 4, '1', '2', '3', '4']:
            search_word = input('Слово для поиска:')
            for item in file:
                if search_word in item[int(search_column) - 1]:
                    print(item)
                    break
            else:
                print('Такого слова в справочнике нет \n')
        else:
            print('Где-то Вы ошиблись с цифрой, попробуем еще')

    elif search_mode in ('2', 2):
        search_word = input('Какое слово ищете?')
        for row in file:
            if search_word in row:
                print(row)
                break
        else:
            print('Такого слова в справочнике нет')
    else:
        print('Вы что-то не то нажали, давайте по-новой \n')


def update():
    """Обновление информации в справочнике"""
    update_info = input('Введите Имя или ID персонажа, в которое бы хотели внести изменения')
    file_data = list(read())
    update_column = input('Вы хотели бы изменить: 1 - Имя, 2 - Телефон, 3 - Комментарий ?')
    update_data = input('Введите новое значение поля')
    if update_column in [1, 2, 3, '1', '2', '3']:
        for row in file_data:
            if str(update_info) == row[0] or str(update_info) == row[1]:
                row[int(update_column)] = str(update_data)
                break
        else:
            print('Такого персонажа не найдено \n')
        with open('directory_enquiries.csv', 'w', newline='', encoding='UTF-8') as file_update:
            writer = csv.writer(file_update)
            writer.writerows(file_data)
    else:
        print('Вы что-то не то нажали, давайте по-новой \n')


def delete():
    """Удаление контакта в справочнике"""
    delete_info = input('Введите имя персонажа или ID, которого хотите удалить ')
    file_data = list(read())
    with open('directory_enquiries.csv', 'w', newline='', encoding='UTF-8') as file_delete:
        writer = csv.writer(file_delete)
        for row in file_data:
            if str(delete_info) != row[0] and str(delete_info) != row[1]:
                writer.writerow(row)


def save():
    """сохранение файла со справочником"""
    save_name = input('Под каким именем сохранить?')
    file = read()
    with open(f'{save_name}.csv', 'w', newline='', encoding='UTF-8') as file_save:
        writer = csv.writer(file_save)
        for row in file:
            writer.writerow(row)
