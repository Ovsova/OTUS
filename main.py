from moduls import actions


def main():
    print('Что бы Вы хотели сделать? \nВведите номер необходимого действия:')
    input_number = 0
    while input_number != '7':
        input_number = input("1 - Показать все контакты \n2 - Создать новый контакт \n3 - Найти контакт \n4 - "
                             "Изменить контакт \n5 - Удалить контакт \n6 - Сохранить файл \n7 - Выход")
        if input_number == '1':
            actions.show_all()
        elif input_number == '2':
            actions.add_new()
        elif input_number == '3':
            actions.search()
        elif input_number == '4':
            actions.update()
        elif input_number == '5':
            actions.delete()
        elif input_number == '6':
            actions.save()
        else:
            print('Введите одну из предложенных команд')


if __name__ == '__main__':
    main()
