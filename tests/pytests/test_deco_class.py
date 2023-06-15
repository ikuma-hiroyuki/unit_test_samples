""" pytest で書いたテストコード(クラスベース - fixture, pytest.mark.parametrize 使用) """
import pytest

from zodiac import (
    get_zodiac_part_dict,
    get_first_month_day_of_zodiac_sign,
    create_zodiac_full_dict,
    get_zodiac_sign_name_dict,
    get_zodiac_sign_name,
)


class TestFixtureClass:
    """ get_first_month_day_of_zodiac_sign のテスト """

    # autouse=True が指定されると、このクラス内のテストメソッドが実行されるたびに、
    # このフィクスチャを自動的に呼び出されます
    @pytest.fixture(autouse=True)
    def setup(self):
        """ テストのセットアップ """

        # テストメソッドの前処理がある場合はここに記述します
        self.zodiac_part_dict = get_zodiac_part_dict()

        yield

        # テストメソッドの後処理がある場合はここに記述します

    def test_month_1(self):
        """ 1月についてテスト """
        result = get_first_month_day_of_zodiac_sign(1, self.zodiac_part_dict)
        assert result == {'month': 12, 'day': 22}

    def test_month_2(self):
        """ 中間の月の代表値として、2月についてテスト """
        result = get_first_month_day_of_zodiac_sign(2, self.zodiac_part_dict)
        assert result == {'month': 1, 'day': 20}

    def test_month_12(self):
        """ 12月についてテスト """
        result = get_first_month_day_of_zodiac_sign(12, self.zodiac_part_dict)
        assert result == {'month': 11, 'day': 22}

    def test_raise(self):
        """ raise ValueError('Invalid month') """
        with pytest.raises(ValueError):
            get_first_month_day_of_zodiac_sign(0, self.zodiac_part_dict)


class TestGetZodiacSignNameDict:
    """ get_zodiac_sign_name_dict のテスト """

    @pytest.fixture(autouse=True)
    def setup(self):
        """ テストのセットアップ """

        # テストメソッドの前処理がある場合はここに記述します
        zodiac_part_dict = get_zodiac_part_dict()
        self.zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        yield

        # テストメソッドの後処理がある場合はここに記述します

    def test_first_day_of_year(self):
        """ 年初の山羊座の最終日前についてテスト """
        result = get_zodiac_sign_name_dict(1, 1, self.zodiac_full_dict)
        assert result == '山羊座'

    def test_last_day_of_capricorn(self):
        """ 山羊座の最終日についてテスト """
        result = get_zodiac_sign_name_dict(1, 19, self.zodiac_full_dict)
        assert result == '山羊座'

    def test_first_day_of_aquarius(self):
        """ 水瓶座の開始日についてテスト """
        result = get_zodiac_sign_name_dict(1, 20, self.zodiac_full_dict)
        assert result == '水瓶座'

    def test_mid_day_of_aquarius(self):
        """ 水瓶座の中間日についてテスト"""
        result = get_zodiac_sign_name_dict(1, 25, self.zodiac_full_dict)
        assert result == '水瓶座'

    def test_last_day_of_year(self):
        """ 年末の射手座最終日以降についてテスト """
        result = get_zodiac_sign_name_dict(12, 25, self.zodiac_full_dict)
        assert result == '山羊座'

    def test_raise(self):
        """ 不正な日付で例外が発生することを確認する """
        with pytest.raises(ValueError):
            get_zodiac_sign_name_dict(13, 31, self.zodiac_full_dict)


class TestParametrize:
    """ @pytest.mark.parametrize のサンプル """

    # 同じ構造のテストを複数実行する場合は、以下のような抽象化された書き方もできます。
    # 第一引数では、 ["month", "day", "expected"] のようなリストを渡すことも可能です。
    @pytest.mark.parametrize("month, day, expected", [
        (1, 1, '山羊座'),
        (1, 19, '山羊座'),
        (1, 20, '水瓶座'),
        (1, 25, '水瓶座'),
        (12, 25, '山羊座'),
    ])
    def test_mark_parametrized_str(self, month, day, expected):
        """ 様々な日付について連続的にテスト
        年初の山羊座の最終日前   :  1月 1日
        山羊座の最終日          :  1月19日
        水瓶座の開始日          :  1月20日
        水瓶座の中間日          :  2月 9日
        年末の射手座の最終日以降 : 12月25日
        """
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(month, day, zodiac_full_dict)
        assert result == expected


class TestParametrizeIterable:
    """ @pytest.mark.parametrize のサンプル(第一引数に iterable を使用) """

    # 第一引数では、 ["month", "day", "expected"] のようなに iterable を渡すことも可能です。
    @pytest.mark.parametrize(["month", "day", "expected"], [
        (1, 1, '山羊座'),
        (1, 19, '山羊座'),
        (1, 20, '水瓶座'),
        (1, 25, '水瓶座'),
        (12, 25, '山羊座'),
    ])
    def test_mark_parametrized_iterable(self, month, day, expected):
        zodiac_part_dict = get_zodiac_part_dict()
        zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        result = get_zodiac_sign_name_dict(month, day, zodiac_full_dict)
        assert result == expected


class TestGetZodiacSignName:
    """ get_zodiac_sign_name のテスト """

    @pytest.fixture(autouse=True)
    def setup(self):
        """ テストのセットアップ """

        # テストメソッドの前処理がある場合はここに記述します
        zodiac_part_dict = get_zodiac_part_dict()
        self.zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

        yield

        # テストメソッドの後処理がある場合はここに記述します

    def test_get_zodiac_sign_name_success(setup):
        """ 日付が不正な値でなければ正常動作することを確認する """
        result = get_zodiac_sign_name(1, 1)
        assert result == '山羊座'

    def test_get_zodiac_sign_name_raise(setup):
        """ 不正な日付で例外が発生することを確認する """
        with pytest.raises(ValueError):
            get_zodiac_sign_name(13, 31)

    def test_get_zodiac_sign_name_raise_not_with(setup):
        """ with を使わない 例外テストの書き方 """
        pytest.raises(ValueError, get_zodiac_sign_name, 13, 31)
