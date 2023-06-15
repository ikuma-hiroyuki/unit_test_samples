""" unittest が異常終了する場合のサンプル """
import inspect
import unittest


class TestRaiseSample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ すべてのテストが開始する前に一度だけ呼ばれる """
        print(cls.__name__, 'setUpClass')

    def setUp(self):
        """ 各テストが開始する前に呼ばれる """
        print(self.__class__.__name__, 'setUp')

    def tearDown(self):
        """ テストが異常終了しても呼ばれる """
        method_name = inspect.stack()[0][3]
        print(self.__class__.__name__, method_name)

    @classmethod
    def tearDownClass(cls):
        """ テストが異常終了しても呼ばれる """
        print(cls.__name__, 'tearDownClass')

    def test_ok(self):
        """ 成功するテスト """
        method_name = inspect.stack()[0][3]
        print(self.__class__.__name__, method_name)

        self.assertEqual(1, 1)

    def test_raise1(self):
        """ raise して異常終了 """
        method_name = inspect.stack()[0][3]
        print(self.__class__.__name__, method_name)

        a = 3 / 0
        self.assertEqual(a, 0)

    def test_raise2(self):
        """ raise して異常終了 """
        method_name = inspect.stack()[0][3]
        print(self.__class__.__name__, method_name)

        b = "hoge" + 3
        self.assertEqual(b, "hoge3")

    def test_success(self):
        """ 成功するテスト """
        method_name = inspect.stack()[0][3]
        print(self.__class__.__name__, method_name)

        self.assertEqual(1, 1)
