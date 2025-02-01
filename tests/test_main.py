# from main import main
# from moduls.controller import FileActions as Action
# from moduls import exceptions
# import pytest
#
#
# @pytest.mark.parametrize('input_number, func', [
#     (1, Action.show_all),
#     (2, Action.add_new),
#     (3, Action.search),
#     (4, Action.update),
#     (5, Action.delete),
#     (6, Action.save),
#     (7, exit()),
#     (8, exceptions.MyExceptions('Fail Number')),
#     (0, exceptions.MyExceptions('Fail Number'))
#
# ])
#
# def test_main(input_number, func):
#     result = main(input_number)
#     assert result == func
