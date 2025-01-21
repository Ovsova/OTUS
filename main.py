from moduls import model

"""Файл запуска приложения"""


def main():
    print('Что бы Вы хотели сделать? \nВведите номер необходимого действия:')
    input_number = 0
    while input_number != '7':
        input_number = input("1 - Показать все контакты \n2 - Создать новый контакт \n3 - Найти контакт \n4 - "
                             "Изменить контакт \n5 - Удалить контакт \n6 - Сохранить файл \n7 - Выход")
        action_number = model.InOutData()
        action_number.value = input_number


if __name__ == '__main__':
    main()
