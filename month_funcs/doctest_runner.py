""" doctest で複数モジュールを連続的にテストするスクリプトの例 """
import doctest
from importlib import import_module


def run_doctests():
    # モジュールのファイルパスのリストを用意する
    module_names = ['month_funcs.doctest_ok', 'month_funcs.doctest_ng']

    for module_name in module_names:
        module_name = import_module(module_name)
        result = doctest.testmod(module_name)
        print(module_name.__name__, result)


if __name__ == '__main__':
    run_doctests()
