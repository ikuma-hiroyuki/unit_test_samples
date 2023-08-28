import pytest
from manufacture import (
    create_handle,
    create_seat,
    create_frame,
    create_bumper,
    semifinished_product_interior,
    semifinished_product_exterior,
    create_car
)


class TestSemiFinishedProductInterior:
    """ semifinished_product_interior のテスト"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """ @pytest.fixture を使うことで、テストの前処理を共通化できる"""
        print("\nテストの前処理")
        self.handle_type = 'normal'
        self.seat_type = 'leather'
        self.a = create_handle(self.handle_type)
        self.b = create_seat(self.seat_type)

        print("yield 前")
        yield  # ここでテストを実行する
        print("yield 後")

        print("テストの後処理\n")

    def test_semifinished_product_interior_luxuary(self):
        """半製品その1 内装品が高級品"""
        print("test_semifinished_product_interior_luxuaryがテストを実行する")
        result = semifinished_product_interior(self.handle_type, self.seat_type, True)
        assert result == self.a - self.b
        print("test_semifinished_product_interior_luxuaryがテストを実行した")

    def test_semifinished_product_interior_not_luxuary(self):
        """半製品その1 内装品が高級品以外"""
        print("test_semifinished_product_interior_not_luxuaryがテストを実行する")
        result = semifinished_product_interior(self.handle_type, self.seat_type, False)
        assert result == self.a + self.b
        print("test_semifinished_product_interior_not_luxuaryがテストを実行した")


class TestSemifinishedProductExterior:
    """ semifinished_product_exterior のテスト"""

    @pytest.fixture(autouse=True)
    def preparation(self):
        """テストの前処理"""
        self.frame_type = 'normal'
        self.bumper_type = 'normal'
        self.c = create_frame(self.frame_type)
        self.d = create_bumper(self.bumper_type)

    def test_semifinished_product_exterior_red(self):
        """半製品その2 外装品の色が red"""
        result = semifinished_product_exterior(self.frame_type, self.bumper_type, 'red')
        assert result == self.c * self.d

    def test_semifinished_product_exterior_not_red(self):
        """半製品その2 外装品の色が red 以外"""
        result = semifinished_product_exterior(self.frame_type, self.bumper_type, 'blue')
        assert result == self.c / self.d


class TestCreateCar:
    """ create_car のテスト"""

    handle_type = 'sporty'
    seat_type = 'leather'
    is_luxuary = True
    color_name = 'red'
    frame_type = 'sporty'
    bumper_type = 'sporty'

    @pytest.fixture(autouse=True)
    def preparation(self):
        """テストの前処理"""
        self.interior = semifinished_product_interior(self.handle_type, self.seat_type, self.is_luxuary)
        self.exterior = semifinished_product_exterior(self.frame_type, self.bumper_type, self.color_name)

    def test_create_car_is_sporty_true(self):
        """スポーツカーの場合"""
        result = create_car(self.handle_type, self.seat_type, self.frame_type, self.bumper_type, self.is_luxuary,
                            self.color_name, True)
        assert result == f'カッコイイ車です！価格は{self.interior + self.exterior}万円！'

    def test_create_car_is_sporty_false(self):
        """スポーツカー以外の場合"""
        result = create_car(self.handle_type, self.seat_type, self.frame_type, self.bumper_type, self.is_luxuary,
                            self.color_name, False)
        assert result == f'それなりな車です！価格は{self.interior + self.exterior}万円！'
