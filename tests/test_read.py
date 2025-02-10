from moduls.view import DirectoryData as DD

file_name = 'test3.csv'


def test_read():
    result = [["1", "Джокер", "21423", "смеется"]]
    value_test = DD.read(file_name)
    print('test=  ', value_test)
    assert result == value_test
