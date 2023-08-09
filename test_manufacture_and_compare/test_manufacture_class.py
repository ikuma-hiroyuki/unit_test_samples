from manufacture import create_handle


class TestCreateHandle:
    """ create_handle のテスト"""

    def test_create_handle_normal(self):
        assert create_handle('normal') == 10

    def test_create_handle_sport(self):
        assert create_handle('sport') == 20
