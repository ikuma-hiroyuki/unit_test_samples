from unittest import TestCase

from manufacture import create_handle, create_seat, create_frame, create_bumper, semifinished_product_interior, \
    semifinished_product_exterior, create_car


class TestCreateHandle(TestCase):
    """ create_handle のテスト"""

    def test_create_handle_normal(self):
        result = create_handle('normal')
        self.assertEqual(result, 10)

    def test_create_handle_sport(self):
        result = create_handle('sport')
        self.assertEqual(result, 20)


class TestCreateSeat(TestCase):
    """ create_seat のテスト"""

    def test_create_seat_leather(self):
        result = create_seat('leather')
        self.assertEqual(result, 50)

    def test_create_seat_normal(self):
        result = create_seat('normal')
        self.assertEqual(result, 30)


class TestCreateFrame(TestCase):
    """ create_frame のテスト"""

    def test_create_frame_normal(self):
        result = create_frame('normal')
        self.assertEqual(result, 100)

    def test_create_frame_sport(self):
        result = create_frame('sport')
        self.assertEqual(result, 150)


class TestCreateBumper(TestCase):
    """ create_bumper のテスト"""

    def test_create_bumper_normal(self):
        result = create_bumper('normal')
        self.assertEqual(result, 15)

    def test_create_bumper_sport(self):
        result = create_bumper('sport')
        self.assertEqual(result, 20)


class TestSemiFinishedProductInterior(TestCase):
    """ semifinished_product_interior のテスト"""

    handle_type = 'normal'
    seat_type = 'leather'

    @classmethod
    def setUpClass(cls):
        """テストの前処理"""
        cls.a = create_handle(cls.handle_type)
        cls.b = create_seat(cls.seat_type)

    def test_semifinished_product_interior_is_luxuary_true(self):
        result = semifinished_product_interior(self.handle_type, self.seat_type, True)
        self.assertEqual(result, self.a - self.b)

    def test_semifinished_product_interior_is_luxuary_false(self):
        result = semifinished_product_interior(self.handle_type, self.seat_type, False)
        self.assertEqual(result, self.a + self.b)


class TestSemifinishedProductExterior(TestCase):
    """ semifinished_product_exterior のテスト"""

    frame_type = 'normal'
    bumper_type = 'normal'

    @classmethod
    def setUpClass(cls):
        """テストの前処理"""
        cls.color_name = 'red'
        cls.c = create_frame(cls.frame_type)
        cls.d = create_bumper(cls.bumper_type)

    def test_semifinished_product_exterior_color_name_red(self):
        result = semifinished_product_exterior(self.frame_type, self.bumper_type, self.color_name)
        self.assertEqual(result, self.c * self.d)

    def test_semifinished_product_exterior_color_name_not_red(self):
        result = semifinished_product_exterior(self.frame_type, self.bumper_type, 'blue')
        self.assertEqual(result, self.c / self.d)


class TestCreateCar(TestCase):
    """ create_car のテスト"""

    handle_type = 'normal'
    seat_type = 'leather'
    frame_type = 'normal'
    bumper_type = 'normal'
    is_luxuary = False
    color_name = 'red'

    @classmethod
    def setUpClass(cls):
        """テストの前処理"""
        cls.interior = semifinished_product_interior(cls.handle_type, cls.seat_type, cls.is_luxuary)
        cls.exterior = semifinished_product_exterior(cls.frame_type, cls.bumper_type, cls.color_name)

    def test_create_car_sporty_true(self):
        result = create_car('normal', 'leather', 'normal', 'normal', False, 'red', True)
        self.assertEqual(result, f'カッコイイ車です！価格は{self.interior + self.exterior}万円！')

    def test_create_car_sporty_false(self):
        result = create_car('normal', 'leather', 'normal', 'normal', False, 'red', False)
        self.assertEqual(result, f'それなりな車です！価格は{self.interior + self.exterior}万円！')
