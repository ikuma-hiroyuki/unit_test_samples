""" pytest で書いたテストコード(関数ベース - fixture 使用) """
import pytest

from zodiac import (
    get_zodiac_sign_name_dict, get_zodiac_part_dict, create_zodiac_full_dict
)


@pytest.fixture
def setup():
    """ get_zodiac_sign_name_dict テスト関数が呼び出す fixture """
    # テストメソッドの前処理がある場合はここに記述します
    zodiac_part_dict = get_zodiac_part_dict()
    zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

    yield zodiac_full_dict

    # テストメソッドの後処理がある場合はここに記述します


def test_get_zodiac_sign_name_dict_first_day_of_year(setup):
    """ 年初の山羊座の最終日前についてテスト """
    result = get_zodiac_sign_name_dict(1, 1, setup)
    assert result == '山羊座'


def test_get_zodiac_sign_name_dict_last_day_of_capricorn(setup):
    """ 山羊座の最終日についてテスト """
    result = get_zodiac_sign_name_dict(1, 19, setup)
    assert result == '山羊座'


def test_get_zodiac_sign_name_dict_first_day_of_aquarius(setup):
    """ 水瓶座の開始日についてテスト """
    result = get_zodiac_sign_name_dict(1, 20, setup)
    assert result == '水瓶座'


def test_get_zodiac_sign_name_dict_mid_day_of_aquarius(setup):
    """ 水瓶座の中間日についてテスト"""
    result = get_zodiac_sign_name_dict(1, 25, setup)
    assert result == '水瓶座'


def test_get_zodiac_sign_name_dict_last_day_of_year(setup):
    """ 年末の射手座最終日以降についてテスト """
    result = get_zodiac_sign_name_dict(12, 25, setup)
    assert result == '山羊座'


def test_get_zodiac_sign_name_dict_raise(setup):
    """ 不正な日付で例外が発生することを確認する """
    with pytest.raises(ValueError):
        get_zodiac_sign_name_dict(13, 31, setup)
