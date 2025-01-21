class MyExceptions(Exception):
    """Собственные исключения"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 'Fail Number':
            return f'Введите одно из предложенных значений \n'
        if self.value == 'Empty File':
            return f'Файл пуст \n'
        if self.value == 'Not Found':
            return 'Такого слова в справочнике нет \n'
        if self.value == 'Try again':
            return f'Где-то Вы ошиблись с цифрой, попробуем еще \n'
        else:
            return f'Неизвестная ошибка \n'
