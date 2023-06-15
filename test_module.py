""" コマンドラインからのテスト呼び出しについての説明用のモジュール """
from unittest import TestCase

import pytest

from month_funcs.compare import get_last_month


def test_func():
    """ pytest のテスト関数 """
    assert 1 == 1


class TestPyTestClass:
    """ pytest のテストクラス """

    def test_method(self):
        """ pytest のテストメソッド """
        assert 1 == 1

    def test_method_2(self):
        """ pytest のテストメソッド """
        assert "hoge" == "hoge"


class TestUnitTestClass(TestCase):
    """ unittest のテストクラス """

    def test_method(self):
        """ unittest のテストメソッド """
        self.assertEqual(1, 1)

    def test_method_2(self):
        """ unittest のテストメソッド """
        self.assertIsNone(None)


class TestUnitTestMethodSample(TestCase):
    """ get_zodiac_sign_name_dict のテスト """

    @classmethod
    def setUpClass(cls):
        # super().setUpClass()
        print('\nsetUpClass は一度だけ実行されます')

    def setUp(self):
        print('\nsetUp はテストメソッド毎に実行されます')
        # super().setUp()

    def tearDown(self):
        print('tearDown はテストメソッド毎に実行されます')
        # super().tearDown()

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass は一度だけ実行されます')
        # super().tearDownClass()

    def test_1(self):
        print('test_1')

    def test_2(self):
        print('test_2')

    def test_3(self):
        print('test_3')


class TestGetLastMonth:
    def test_normal(self):
        month = get_last_month(12)
        assert month == 11

    def test_raise(self):
        pytest.raises(ValueError, get_last_month, 0)
