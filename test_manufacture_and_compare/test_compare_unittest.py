from unittest import TestCase

from month_funcs.compare import get_last_month


class TestGetLastMonth(TestCase):
    """get_last_month のテスト"""

    @classmethod
    def setUpClass(cls):
        """テストクラスの前処理"""
        print('テストクラスの前処理\n')

    @classmethod
    def tearDownClass(cls):
        """テストクラスの後処理"""
        print('\nテストクラスの後処理')

    def setUp(self):
        """テストの前処理"""
        print('\nテストメソッドの前処理')

    def tearDown(self):
        """テストの後処理"""
        print('テストメソッドの後処理\n')

    def test_raise_type_error(self):
        """異常系でint型でない場合"""
        print('test_raise_type_error')
        with self.assertRaises(TypeError):
            get_last_month('1')

    def test_raise_value_error_over_12(self):
        """異常系で12より大きい場合"""
        print('test_raise_value_error_over_12')
        with self.assertRaises(ValueError):
            get_last_month(13)

    def test_raise_value_error_under_1(self):
        """異常系で1より小さい場合"""
        print('test_raise_value_error_under_1')
        with self.assertRaises(ValueError):
            get_last_month(0)

    def test_normal_1(self):
        """正常系で1月の場合"""
        print('test_normal_1')
        self.assertEqual(get_last_month(1), 12)

    def test_normal_other_then_1(self):
        """正常系で1月でない場合"""
        print('test_normal_other_then_1')
        self.assertEqual(get_last_month(2), 1)
