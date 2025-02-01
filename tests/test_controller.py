from moduls.controller import FileActions
from moduls.view import DirectoryData as DD

def test_show_all():
    result = [["1","Росомаха","325235","да не умер он"]]
    value_test = DD.read('test.csv')
    print('test=  ',value_test )
    print('!', FileActions.show_all(value_test))
    assert result == FileActions.show_all(value_test)