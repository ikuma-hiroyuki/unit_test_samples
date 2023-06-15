import pytest

from month_funcs.compare import get_last_month, get_last_month_concised


# get_last_month のすべての条件分岐についてのテスト群
def test_not_int():
    """ 整数以外はエラー """
    with pytest.raises(TypeError):
        get_last_month('hoge')


def test_month_0():
    """ 0月はエラー """
    with pytest.raises(ValueError):
        get_last_month(0)


def test_over_month():
    """ 13月はエラー """
    with pytest.raises(ValueError):
        get_last_month(13)


def test_january():
    """ 1月の前月は12月 """
    assert get_last_month(1) == 12


def test_february():
    """ 1月以外の任意の月でテスト """
    assert get_last_month(2) == 1


# get_last_month_concised のいちおうすべての条件分岐についてのテスト群
def test_raise():
    """ 例外が発生するケース """
    with pytest.raises(ValueError):
        get_last_month_concised(0)


def test_success():
    """ 戻り値を得られるケース """
    assert get_last_month_concised(2) == 1

# get_last_month_concised の本来望ましいすべての条件分岐についてのテスト群
# def test_concise_not_int():
#     """ 整数以外はエラー """
#     with pytest.raises(TypeError):
#         get_last_month_concised('hoge')
#
#
# def test_concise_month_0():
#     """ 0月はエラー """
#     with pytest.raises(ValueError):
#         get_last_month_concised(0)
#
#
# def test_concise_over_month():
#     """ 13月はエラー """
#     with pytest.raises(ValueError):
#         get_last_month_concised(13)
#
#
# def test_concise_january():
#     """ 1月の前月は12月 """
#     assert get_last_month_concised(1) == 12
#
#
# def test_concise_february():
#     """ 1月以外の任意の月でテスト """
#     assert get_last_month_concised(2) == 1
