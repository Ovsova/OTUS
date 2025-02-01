# from moduls import exceptions, model
# from moduls.view import DirectoryData as DD
from moduls.controller import FileActions as Action
from moduls.model import InOutData

def test_value():
    result = InOutData.value.setter(1)
    assert result == Action.show_all()