""" unittest で書いたテストコード """
import unittest

from zodiac import (
    get_zodiac_part_dict,
    get_first_month_day_of_zodiac_sign,
    create_zodiac_full_dict,
    get_zodiac_sign_name_dict, get_zodiac_sign_name,
)


class TestGetFirstMonthDayOfZodiacSign(unittest.TestCase):
    """ get_first_month_day_of_zodiac_sign のテスト

    年の切り替わりになる1月, 12月と、それ以外の月と、例外についてテストする　"""

    def setUp(self):
        """ setUp は各テストメソッドの実行前に実行される """
        self.zodiac_part_dict = get_zodiac_part_dict()

    def test_success(self):
        """ 正常系のテスト
        subtest の紹介という意味で書いてはみたが、
        テストが3つくらいしかなく個々のメソッドの行数も少ないならば、
        個別に書いたほうが視認性も高く良いだろう """
        test_cases = [
            (1, 12, 22),
            (2, 1, 20),
            (12, 11, 22),
        ]
        for month, expected_month, expected_day in test_cases:
            with self.subTest(month=month, expected_month=expected_month, expected_day=expected_day):
                result = get_first_month_day_of_zodiac_sign(month, self.zodiac_part_dict)
                self.assertEqual(result, {'month': expected_month, 'day': expected_day})

    def test_raise(self):
        """ raise ValueError('Invalid month') """
        with self.assertRaises(ValueError):
            get_first_month_day_of_zodiac_sign(0, self.zodiac_part_dict)


class TestGetZodiacSignNameDict(unittest.TestCase):
    """ get_zodiac_sign_name_dict のテスト """

    @classmethod
    def setUpClass(cls):
        zodiac_part_data = get_zodiac_part_dict()
        cls.zodiac_full_dict = create_zodiac_full_dict(zodiac_part_data)

    def test_values(self):
        """ 様々な日付について連続的にテスト
        年初の山羊座の最終日前   :  1月 1日
        山羊座の最終日          :  1月19日
        水瓶座の開始日          :  1月20日
        水瓶座の中間日          :  2月 9日
        年末の射手座の最終日以降 : 12月25日
        """
        test_cases = [
            (1, 1, '山羊座'),
            (1, 19, '山羊座'),
            (1, 20, '水瓶座'),
            (1, 25, '水瓶座'),
            (12, 25, '山羊座'),
        ]
        for month, day, expected in test_cases:
            with self.subTest(month=month, day=day):
                result = get_zodiac_sign_name_dict(month, day, self.zodiac_full_dict)
                self.assertEqual(result, expected)


class TestGetZodiacSignName(unittest.TestCase):
    """ get_zodiac_sign_name のテスト """

    def test_values(self):
        """ 様々な日付について連続的にテスト
        年初の山羊座の最終日前   :  1月 1日
        山羊座の最終日          :  1月19日
        水瓶座の開始日          :  1月20日
        水瓶座の中間日          :  2月 9日
        年末の射手座の最終日以降 : 12月25日
        """
        test_cases = [
            (1, 1, '山羊座'),
            (1, 19, '山羊座'),
            (1, 20, '水瓶座'),
            (1, 25, '水瓶座'),
            (12, 25, '山羊座'),
        ]
        for month, day, expected in test_cases:
            with self.subTest(month=month, day=day):
                result = get_zodiac_sign_name(month, day)
                self.assertEqual(result, expected)
