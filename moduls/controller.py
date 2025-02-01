import csv
from moduls import exceptions

"""Операции со справочником"""


class FileActions:

    def show_all(data):
        data_list = []
        """Отображение всего содержимого справочника"""
        for line in data:
            data_list.append(line)
            if len(line) != 0:
                print(line[1:])
            else:
                raise exceptions.MyExceptions('Empty File')
        return data_list

    def add_new(data):
        """добавить новый контакт в справочник"""
        # file = read()
        pers_count = sum(1 for row in data)
        with open('directory_enquiries.csv', 'a', encoding='UTF-8') as file:
            new_pers_long = str(pers_count + 1)
            new_pers_name = input('Введите Имя')
            new_pers_number = input('Введите номер')
            new_pers_comment = input('Введите комментарий к персонажу')
            file.writelines([new_pers_long, ',', new_pers_name, ',', new_pers_number, ',', new_pers_comment])
            file.writelines('\n')

    def search(data):
        """Поиск информации в справочнике"""
        # file = read()
        search_mode = input('Хотите поиск по полям, жмите 1, \nЕсли общий, то жмакайте 2')
        if search_mode == '1':
            print('По какому полю хотите найти?')
            search_column = input('1 - ID персонажа, 2 - Имя персонажа, 3 - Номер телефона, 4 - Внезапно Комментарий')
            if search_column in ['1', '2', '3', '4']:
                search_word = input('Слово для поиска:')
                for item in data:
                    if search_word in item[int(search_column) - 1]:
                        print(item)
                        break
                else:
                    raise exceptions.MyExceptions('Not Found')
            else:
                raise exceptions.MyExceptions('Try again')

        elif search_mode == '2':
            search_word = input('Какое слово ищете?')
            for row in data:
                if search_word in row:
                    print(row)
                    break
            else:
                raise exceptions.MyExceptions('Not Found')
        else:
            raise exceptions.MyExceptions('Try again')

    def update(data):
        """Обновление информации в справочнике"""
        update_info = input('Введите Имя или ID персонажа, в которое бы хотели внести изменения')
        cur_data = list(data)
        update_column = input('Вы хотели бы изменить: 1 - Имя, 2 - Телефон, 3 - Комментарий ?')
        update_data = input('Введите новое значение поля')
        if update_column in ['1', '2', '3']:
            for row in cur_data:
                if str(update_info) == row[0] or str(update_info) == row[1]:
                    row[int(update_column)] = str(update_data)
                    break
            else:
                raise exceptions.MyExceptions('Not Found')
            with open('directory_enquiries.csv', 'w', newline='', encoding='UTF-8') as file_update:
                writer = csv.writer(file_update)
                writer.writerows(cur_data)
        else:
            raise exceptions.MyExceptions('Try again')

    def delete(data):
        """Удаление контакта в справочнике"""
        delete_info = input('Введите имя персонажа или ID, которого хотите удалить ')
        cur_data = list(data)
        with open('directory_enquiries.csv', 'w', newline='', encoding='UTF-8') as file_delete:
            writer = csv.writer(file_delete)
            for row in cur_data:
                if str(delete_info) != row[0] and str(delete_info) != row[1]:
                    writer.writerow(row)

    def save(data):
        """сохранение файла со справочником"""
        save_name = input('Под каким именем сохранить?')
        # file = read()
        with open(f'{save_name}.csv', 'w', newline='', encoding='UTF-8') as file_save:
            writer = csv.writer(file_save)
            for row in data:
                writer.writerow(row)
