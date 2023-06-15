def get_last_month(month):
    """ 指定された月の前月を取得する """
    if not isinstance(month, int):
        raise TypeError('月は整数で指定してください')
    if month < 1:
        raise ValueError('月は1以上で指定してください')
    if month > 12:
        raise ValueError('月は12以下で指定してください')

    if month == 1:
        return 12
    else:
        return month - 1


def get_last_month_concised(month):
    """ 指定された月の前月を取得する。(簡略番) """
    if not 1 <= month <= 12:
        raise ValueError('月は1-12の範囲で指定してください')

    return 12 if month == 1 else month - 1
