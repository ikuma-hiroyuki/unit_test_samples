import doctest

from month_funcs import doctest_ok


def load_tests(loader, tests, ignore):
    """ロードされたテストスイートにドックストリングテストを追加する関数

    :param loader: テストローダー
    :param tests: テストスイート
    :param ignore: 無視する要素
    :return: 追加されたテストスイート
    """
    # print(__name__)
    #
    # print('loader: {}'.format(loader))
    # print('tests: {}'.format(tests))
    # print('ignore: {}'.format(ignore))

    # ドックストリングテスト用のテストスイートを作成する
    test_suites = doctest.DocTestSuite(doctest_ok)

    # ロードされたテストスイートにドックストリングテストを追加する
    tests.addTests(test_suites)

    # print('tests: {}'.format(tests))

    return tests
