""" コマンドラインからのテスト呼び出しについての説明用のモジュール """
from unittest import TestCase


def test_func():
    """ pytest のテスト関数 """
    assert 2 == 2


class TestPyTestClass:
    """ pytest のテストクラス """

    def test_method(self):
        """ pytest のテストメソッド """
        assert 2 == 2

    def test_method_2(self):
        """ pytest のテストメソッド """
        assert "hoge" == "hoge"


class TestUnitTestClass(TestCase):
    """ unittest のテストクラス """

    def test_method(self):
        """ unittest のテストメソッド """
        self.assertEqual(2, 2)

    def test_method_2(self):
        """ unittest のテストメソッド """
        self.assertIsNone(None)
