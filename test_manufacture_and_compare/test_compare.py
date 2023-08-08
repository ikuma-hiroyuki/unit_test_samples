import pytest

from month_funcs.compare import get_last_month, get_last_month_concised


def test_get_last_month_normal():
    """正常系で1月でない場合"""
    assert get_last_month(2) == 1


def test_get_last_month_12():
    """正常系で1月の場合"""
    assert get_last_month(1) == 12


def test_get_last_month_over_12():
    """異常系で12より大きい場合"""
    with pytest.raises(ValueError):
        get_last_month(13)


def test_get_last_month_over_12_not_with():
    """異常系で12より大きい場合"""
    pytest.raises(ValueError, get_last_month, 13)


def test_get_last_month_under_1():
    """異常系で1より小さい場合"""
    with pytest.raises(ValueError):
        get_last_month(0)


def test_get_last_month_not_int():
    """異常系でint型でない場合"""
    with pytest.raises(TypeError):
        get_last_month('1')
