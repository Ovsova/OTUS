from moduls import exceptions
from moduls.view import DirectoryData as DD
from moduls.controller import FileActions as Action


class InOutData(DD):
    """Выбор функционала справочника"""

    def __init__(self):
        self._value = []
        self.filename = 'directory_enquiries.csv'


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, number):
        self._value = DD.read(self.filename)
        if number == '1':
            Action.show_all(self._value)
        elif number == '2':
            Action.add_new(self._value, self.filename)
        elif number == '3':
            Action.search(self._value)
        elif number == '4':
            Action.update(self._value)
        elif number == '5':
            Action.delete(self._value, self.filename)
        elif number == '6':
            Action.save(self._value)
        else:
            print('Введите цифру из списка')
