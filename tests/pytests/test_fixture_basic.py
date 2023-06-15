import pytest


@pytest.fixture
def setup():
    print('\nsetup が前処理を開始します')
    # ここでテスト関数の前処理を行う

    yield  # yield は「処理を中断して呼び出し元に戻る」という意味の文です

    print('\nsetup が後処理を開始します')
    # ここでテスト関数の後処理を行う


def test_function1(setup):
    print('test_function1 内部の処理を開始します')
    assert 1 == 1
    print('test_function1 内部の処理が終了しました')


def test_function2(setup):
    print('test_function2 内部の処理を開始します')
    assert 2 == 2
    print('test_function2 内部の処理が終了しました')
