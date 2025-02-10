from moduls.controller import FileActions
from moduls.view import DirectoryData as DD
import pytest
from unittest.mock import patch
import csv
from moduls.exceptions import MyExceptions
import os
import atexit

"""Тестирование реализовано разлисными вариациями"""


file_test = 'test.csv'
file_test1 = 'test1.csv'
file_test2 = 'test2.csv'

"""Тестирование функции отображения всего справочника"""
@pytest.mark.parametrize('text,  enquiries', [
    (DD.read(file_test), [["1", "Росомаха", "325235", "да не умер он"]]),
    (DD.read(file_test1), [["1", "Росомаха", "325235", "да не умер он"], ["2", "Доктор", "125341233", "Кто?"]]),
])
def test_show_all(text, enquiries):
    assert FileActions.show_all(text) == enquiries


def test_add_new1():
    with patch('builtins.input', side_effect=['Женщина-Кошка', '413523', 'Мурр']):
        new_line = FileActions.add_new(DD.read(file_test2), file_test2)
    result = [["1", "Росомаха", "325235", "да не умер он"], ["2", "Женщина-Кошка", "413523", "Мурр"]]
    assert DD.read(file_test2) == result


def test_add_new2():
    with patch('builtins.input', side_effect=['Гром', '1234', 'Майор']):
        new_line = FileActions.add_new(DD.read(file_test2), file_test2)
    result = [["1", "Росомаха", "325235", "да не умер он"], ["2", "Женщина-Кошка", "413523", "Мурр"],
              ["3", "Гром", "1234", "Майор"]]
    assert DD.read(file_test2) == result

"""Тестирование функции удаления контакта из справочника"""
def test_delete1():
    with patch('builtins.input', return_value='Гром'):
        delete_line1 = FileActions.delete(DD.read(file_test2), file_test2)
    result = [["1", "Росомаха", "325235", "да не умер он"], ["2", "Женщина-Кошка", "413523", "Мурр"]]
    assert DD.read(file_test2) == result


def test_delete2():
    with patch('builtins.input', return_value='2'):
        delete_line2 = FileActions.delete(DD.read(file_test2), file_test2)
    result = [["1", "Росомаха", "325235", "да не умер он"]]
    assert DD.read(file_test2) == result

"""Тестирование функции поиска по справочнику"""
def test_search1(capfd):
    filepath = 'new_test_search.csv'
    kontact = [['1', 'Гослинг', '523451', 'Сами все знаете'],
               ['2', 'Данте', '5462234236', 'Сомнительный брат'],
               ['3', 'Вергилий', '5462234237', 'Тот самый сомнительный брат']
               ]
    with open(filepath, 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=',',
                                lineterminator='\n')
        for line in kontact:
            csv_writer.writerow(line)

    file_read = open(filepath, 'r', encoding='UTF-8')
    file_reader = list(csv.reader(file_read, dialect='excel', delimiter=','))
    with patch('builtins.input', side_effect=['2', 'Данте']):
        FileActions.search(kontact)
        captured = capfd.readouterr()

        # print(captured.out)
        result = "['2', 'Данте', '5462234236', 'Сомнительный брат']"
        assert result in captured.out


def test_search2(capfd):
    filepath = 'new_test_search.csv'
    kontact = [['1', 'Гослинг', '523451', 'Сами все знаете'],
               ['2', 'Данте', '5462234236', 'Сомнительный брат'],
               ['3', 'Вергилий', '5462234237', 'Тот самый сомнительный брат']
               ]
    with open(filepath, 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=',',
                                lineterminator='\n')
        for line in kontact:
            csv_writer.writerow(line)

    file_read = open(filepath, 'r', encoding='UTF-8')
    file_reader = list(csv.reader(file_read, dialect='excel', delimiter=','))
    with patch('builtins.input', side_effect=['1', '1', '3']):
        FileActions.search(kontact)
        captured = capfd.readouterr()

        # print(captured.out)
        result = "['3', 'Вергилий', '5462234237', 'Тот самый сомнительный брат']"
        assert result in captured.out


def test_search_exception():
    filepath = 'new_test_search.csv'
    kontact = [['1', 'Гослинг', '523451', 'Сами все знаете'],
               ['2', 'Данте', '5462234236', 'Сомнительный брат'],
               ['3', 'Вергилий', '5462234237', 'Тот самый сомнительный брат']
               ]
    with open(filepath, 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=',',
                                lineterminator='\n')
        for line in kontact:
            csv_writer.writerow(line)

    file_read = open(filepath, 'r', encoding='UTF-8')
    file_reader = list(csv.reader(file_read, dialect='excel', delimiter=','))
    try:
        with patch('builtins.input', side_effect=['3']):
            FileActions.search(file_reader)
    except MyExceptions as e:
        assert str(e) == 'Где-то Вы ошиблись с цифрой, попробуем еще \n'

"""Тестирование функции обновления информации в справочнике"""
def test_update():
    filepath = 'new_test_update.csv'
    kontact = [['1', 'Гослинг', '523451', 'Сами все знаете'],
               ['2', 'Данте', '5462234236', 'Сомнительный брат'],
               ['3', 'Вергилий', '5462234237', 'Тот самый сомнительный брат']
               ]
    with open(filepath, 'w', encoding='UTF-8') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel', delimiter=',',
                                lineterminator='\n')
        for line in kontact:
            csv_writer.writerow(line)

    file_read = open(filepath, 'r', encoding='UTF-8')
    file_reader = list(csv.reader(file_read, dialect='excel', delimiter=','))

    with patch('builtins.input', side_effect=['Данте', '3', 'У него сомнительный брат']):
        FileActions.update(file_reader, filepath)

    with open(filepath, 'r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    print(data)
    assert data[0] == ['1', 'Гослинг', '523451', 'Сами все знаете']
    assert data[1] == ['2', 'Данте', '5462234236', 'У него сомнительный брат']
    assert data[2] == ['3', 'Вергилий', '5462234237', 'Тот самый сомнительный брат']

"""Удаление, создаваеммых внутри тестов, файлов"""
def delete_test_file():
    os.remove('new_test_update.csv')
    os.remove('new_test_search.csv')
atexit.register(delete_test_file)
