""" pytest で書いたテストコード(クラスベース) """
import pytest

from zodiac import (
    get_zodiac_part_dict,
    get_first_month_day_of_zodiac_sign,
    create_zodiac_full_dict,
    get_zodiac_sign_name_dict, get_zodiac_sign_name,
)


class TestZodiacPartData:
    """ get_zodiac_part_dict のテスト"""

    def test_success(self):
        """ ファイルを読んで辞書を生成できることを確認できればOK """
        result = get_zodiac_part_dict()

        assert isinstance(result, dict)
        assert result['山羊座'] == {'month': 1, 'day': 19}


class TestGetFirstMonthDayOfZodiacSign:
    """ get_first_month_day_of_zodiac_sign のテスト """

    def test_month_1(self):
        """ 1月についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()

        result = get_first_month_day_of_zodiac_sign(1, zodiac_part_dict)
        assert result == {'month': 12, 'day': 22}

    def test_month_2(self):
        """ 中間の月の代表値として、2月についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()

        result = get_first_month_day_of_zodiac_sign(2, zodiac_part_dict)
        assert result == {'month': 1, 'day': 20}

    def test_month_12(self):
        """ 12月についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()

        result = get_first_month_day_of_zodiac_sign(12, zodiac_part_dict)
        assert result == {'month': 11, 'day': 22}

    def test_raise(self):
        """ raise ValueError('Invalid month') """
        zodiac_part_dict = get_zodiac_part_dict()

        with pytest.raises(ValueError):
            get_first_month_day_of_zodiac_sign(0, zodiac_part_dict)


class TestCreateZodiacTermDict:
    """ create_zodiac_term_dict のテスト """

    def test_success(self):
        """ create_zodiac_full_dict の戻り値のテスト """
        zodiac_part_dict = get_zodiac_part_dict()

        result = create_zodiac_full_dict(zodiac_part_dict)

        # 得られた辞書内の値のうちいくつかを調べてみる
        assert result['山羊座']['from'] == {'month': 12, 'day': 22}
        assert result['山羊座']['to'] == {'month': 1, 'day': 19}

        assert result['水瓶座']['from'] == {'month': 1, 'day': 20}
        assert result['水瓶座']['to'] == {'month': 2, 'day': 18}

        assert result['射手座']['from'] == {'month': 11, 'day': 22}
        assert result['射手座']['to'] == {'month': 12, 'day': 21}


class TestGetZodiacSignNameDict:
    """ get_zodiac_sign_name_dict のテスト """

    def test_first_day_of_year(self):
        """ 年初の山羊座の最終日前についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(1, 1, zodiac_full_dict)
        assert result == '山羊座'

    def test_last_day_of_capricorn(self):
        """ 山羊座の最終日についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(1, 19, zodiac_full_dict)
        assert result == '山羊座'

    def test_first_day_of_aquarius(self):
        """ 水瓶座の開始日についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(1, 20, zodiac_full_dict)
        assert result == '水瓶座'

    def test_mid_day_of_aquarius(self):
        """ 水瓶座の中間日についてテスト"""
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(1, 25, zodiac_full_dict)
        assert result == '水瓶座'

    def test_last_day_of_year(self):
        """ 年末の射手座最終日以降についてテスト """
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(12, 25, zodiac_full_dict)
        assert result == '山羊座'

    def test_raise(self):
        """ 不正な日付で例外が発生することを確認する """
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        with pytest.raises(ValueError):
            get_zodiac_sign_name_dict(13, 31, zodiac_full_dict)


class TestGetZodiacSignName:
    """ get_zodiac_sign_name のテスト """

    def test_success(self):
        """ 日付が不正な値でなければ正常動作することを確認する """
        result = get_zodiac_sign_name(1, 1)
        assert result == '山羊座'

    def test_raise(self):
        """ 不正な日付で例外が発生することを確認する """
        with pytest.raises(ValueError):
            get_zodiac_sign_name(13, 31)

    def test_raise_not_with(self):
        """ with を使わない 例外テストの書き方 """
        pytest.raises(ValueError, get_zodiac_sign_name, 13, 31)
