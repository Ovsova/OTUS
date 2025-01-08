from moduls import actions


def main():
    print('Что бы Вы хотели сделать? \nВведите номер необходимого действия:')
    while True:
        input_number = input("1 - Показать все контакты \n2 - Создать новый контакт \n3 - Найти контакт \n4 - "
                             "Изменить контакт \n5 - Удалить контакт \n6 - Сохранить файл \n7 - Выход")
        if input_number in ('1', 1):
            print('1')
            actions.show_all()
        if input_number in ('2', 2):
            print('2')
            actions.add_new()
        if input_number in ('3', 3):
            print('3')
            actions.search()
        if input_number in ('4', 4):
            print('4')
            actions.update()
        if input_number in ('5', 5):
            actions.delete()
        if input_number in ('6', 6):
            actions.save()
        if input_number in ('7', 7):
            exit()
        else:
            print('Введите одну из предложенных команд')


if __name__ == '__main__':
    main()
