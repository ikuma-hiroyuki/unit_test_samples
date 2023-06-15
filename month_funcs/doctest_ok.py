def get_last_month(month):
    """ 指定された月の前月を取得する。(簡略番)

    :param month: 月を表す整数
    :return: 月を表す整数

    >>> get_last_month(1)
    12
    >>> get_last_month(2)
    1
    >>> get_last_month(7)
    6
    >>> get_last_month(13)
    Traceback (most recent call last):
        ...
    ValueError: 月は1-12の範囲で指定してください
    """
    if not isinstance(month, int):
        raise TypeError('月は整数で指定してください')
    if month < 1:
        raise ValueError('月は1-12の範囲で指定してください')
    if month > 12:
        raise ValueError('月は1-12の範囲で指定してください')

    if month == 1:
        return 12
    else:
        return month - 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
