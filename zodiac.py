"""日付から星座を判定するプログラム """
import csv
from datetime import date
from pathlib import Path


def get_zodiac_part_dict():
    """resources/zodiac.csv から dictReader によってデータを取得する

    :return: 'name': {'month': 1, 'day': 20} という形式の要素を持つ辞書
    """
    path = Path(__file__).resolve().parent / 'resources' / 'zodiac.csv'

    result_dict = {}
    with path.open(encoding='utf-8') as f:
        reader: csv.DictReader = csv.DictReader(f)
        for row in reader:
            result_dict[row['星座名']] = {"month": int(row['月']), "day": int(row['日'])}
    return result_dict


def get_first_month_day_of_zodiac_sign(month, zodiac_part_dict):
    """各星座の最終日を含む月から、その星座の最初の日を返す

    :return: {'month': 1, 'day': 20} といった形式の辞書
    """
    if month == 1:
        last_month = 12
    else:
        last_month = month - 1

    for v in zodiac_part_dict.values():
        if v['month'] == last_month:
            return {'month': last_month, 'day': v['day'] + 1, }
    raise ValueError('Invalid month')


def create_zodiac_full_dict(zodiac_part_dict):
    """各星座の期間を辞書型で返す

    要素の例: "水瓶座": {'from': {"month": 1, "day": 20}, 'to': {"month": 2, "day": 18}, }
    """
    result_dict = {}
    for k, v in zodiac_part_dict.items():
        result_dict[k] = {
            'from': get_first_month_day_of_zodiac_sign(v['month'], zodiac_part_dict),
            'to': {'month': v['month'], 'day': v['day']},
        }
    return result_dict


def get_zodiac_sign_name_dict(month, day, zodiac_full_dict):
    """日付と辞書を受け取ると、辞書に基づいて、その日付の星座を返す

    :param day: 日
    :param month: 月
    :param zodiac_full_dict: 星座名をキーとし、値には期間を表す辞書を持つ辞書
    :return: 星座名
    """

    for k, v in zodiac_full_dict.items():
        if v['from']['month'] == month:
            if v['from']['day'] <= day:
                return k
        elif v['to']['month'] == month:
            if v['to']['day'] >= day:
                return k
    raise ValueError('誕生日に該当する星座が見つかりませんでした')


def get_zodiac_sign_name(month, day):
    """日付を受け取ると、有効な日付であることを確認し、その日付の星座を返す

    :param day: 日
    :param month: 月
    :return: 星座名
    """
    # その日が存在するかを確認(閏年の2月29日生まれの可能性も考慮)
    date(2020, month, day)  # 不正な month, day の組み合わせだとここで例外が発生する

    zodiac_part_dict = get_zodiac_part_dict()
    zodiac_full_dict = create_zodiac_full_dict(zodiac_part_dict)

    return get_zodiac_sign_name_dict(month, day, zodiac_full_dict)


if __name__ == "__main__":
    input_month = int(input('月を入力してください: '))
    input_day = int(input('日を入力してください: '))

    result = get_zodiac_sign_name(input_month, input_day)
    print(result)
