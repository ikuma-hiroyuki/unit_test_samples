""" unittest で書いたテストコード """
import unittest

from zodiac import (
    get_zodiac_part_dict,
    get_first_month_day_of_zodiac_sign,
    create_zodiac_full_dict,
    get_zodiac_sign_name_dict, get_zodiac_sign_name,
)


class TestZodiacPartData(unittest.TestCase):
    """ get_zodiac_part_dict のテスト"""

    def test_success(self):
        """ ファイルを読んで辞書を生成できることを確認できればOK """
        result = get_zodiac_part_dict()

        self.assertIsInstance(result, dict)
        self.assertEqual(result['山羊座'], {'month': 1, 'day': 19})


class TestGetFirstMonthDayOfZodiacSign(unittest.TestCase):
    """ get_first_month_day_of_zodiac_sign のテスト

    年の切り替わりになる1月, 12月と、それ以外の月と、例外についてテストする　"""

    def setUp(self):
        """ setUp は各テストメソッドの実行前に実行される """
        self.zodiac_part_dict = get_zodiac_part_dict()

    def tearDown(self):
        """ tearDown は各テストメソッドの実行後に実行される """
        print('\ntearDown で特にやりたいことは無いが、コメントだけつけてみた')

    def test_month_1(self):
        """ 1月についてテスト """
        result = get_first_month_day_of_zodiac_sign(1, self.zodiac_part_dict)
        self.assertEqual(result, {'month': 12, 'day': 22})

    def test_month_2(self):
        """ 中間の月の代表値として、2月についてテスト """
        result = get_first_month_day_of_zodiac_sign(2, self.zodiac_part_dict)
        self.assertEqual(result, {'month': 1, 'day': 20})

    def test_month_12(self):
        """ 12月についてテスト """
        result = get_first_month_day_of_zodiac_sign(12, self.zodiac_part_dict)
        self.assertEqual(result, {'month': 11, 'day': 22})

    def test_raise(self):
        """ raise ValueError('Invalid month') """
        with self.assertRaises(ValueError):
            get_first_month_day_of_zodiac_sign(0, self.zodiac_part_dict)


class TestCreateZodiacTermDict(unittest.TestCase):
    """ create_zodiac_term_dict のテスト """

    def test_dict_values(self):
        """ create_zodiac_full_dict の戻り値のテスト """
        zodiac_part_dict = get_zodiac_part_dict()

        result = create_zodiac_full_dict(zodiac_part_dict)

        # 得られた辞書内の値のうちいくつかを調べてみる
        self.assertDictEqual(result['山羊座']['from'], {'month': 12, 'day': 22})
        self.assertDictEqual(result['山羊座']['to'], {'month': 1, 'day': 19})

        self.assertDictEqual(result['水瓶座']['from'], {'month': 1, 'day': 20})
        self.assertDictEqual(result['水瓶座']['to'], {'month': 2, 'day': 18})

        self.assertDictEqual(result['射手座']['from'], {'month': 11, 'day': 22})
        self.assertDictEqual(result['射手座']['to'], {'month': 12, 'day': 21})


class TestGetZodiacSignNameDict(unittest.TestCase):
    """ get_zodiac_sign_name_dict のテスト """

    @classmethod
    def setUpClass(cls):
        zodiac_part_data = get_zodiac_part_dict()
        cls.zodiac_full_dict = create_zodiac_full_dict(zodiac_part_data)

    def test_first_day_of_year(self):
        """ 年初の山羊座の最終日前についてテスト """
        result = get_zodiac_sign_name_dict(1, 1, self.zodiac_full_dict)
        self.assertEqual(result, '山羊座')

    def test_last_day_of_capricorn(self):
        """ 山羊座の最終日についてテスト """
        result = get_zodiac_sign_name_dict(1, 19, self.zodiac_full_dict)
        self.assertEqual(result, '山羊座')

    def test_first_day_of_aquarius(self):
        """ 水瓶座の開始日についてテスト """
        result = get_zodiac_sign_name_dict(1, 20, self.zodiac_full_dict)
        self.assertEqual(result, '水瓶座')

    def test_mid_day_of_aquarius(self):
        """ 水瓶座の中間日についてテスト"""
        result = get_zodiac_sign_name_dict(1, 25, self.zodiac_full_dict)
        self.assertEqual(result, '水瓶座')

    def test_last_day_of_year(self):
        """ 年末の射手座最終日以降についてテスト """
        result = get_zodiac_sign_name_dict(12, 25, self.zodiac_full_dict)
        self.assertEqual(result, '山羊座')

    def test_raise(self):
        """ 不正な日付で例外が発生することを確認する """
        with self.assertRaises(ValueError):
            get_zodiac_sign_name_dict(13, 31, self.zodiac_full_dict)

    def test_raise_no_with(self):
        """  with を使わない 例外テストの書き方 """
        self.assertRaises(
            ValueError, get_zodiac_sign_name_dict, 13, 31, self.zodiac_full_dict)


class TestGetZodiacSignName(unittest.TestCase):
    """ get_zodiac_sign_name のテスト """

    def test_success(self):
        """ 日付が不正な値でなければ正常動作することを確認する """
        result = get_zodiac_sign_name(1, 1)
        self.assertEqual(result, '山羊座')

    def test_raise(self):
        """ 不正な日付で例外が発生することを確認する """
        with self.assertRaises(ValueError):
            get_zodiac_sign_name(13, 31)

    def test_raise_not_with(self):
        """ with を使わない 例外テストの書き方 """
        self.assertRaises(ValueError, get_zodiac_sign_name, 13, 31)
