from manufacture import create_handle, create_seat, create_frame, create_bumper, semifinished_product_interior, \
    semifinished_product_exterior, create_car


def test_create_handle_handle_type_normal():
    """ create_handle の handle_type が normal のときのテスト"""
    assert create_handle('normal') == 10


def test_create_handle_handle_type_not_normal():
    """ create_handle の handle_type が normal 以外のときのテスト"""
    assert create_handle('sporty') == 20


def test_create_seat_seat_type_leather():
    """ create_seat の seat_type が leather のときのテスト"""
    assert create_seat('leather') == 50


def test_create_seat_seat_type_not_leather():
    """ create_seat の seat_type が leather 以外のときのテスト"""
    assert create_seat('normal') == 30


def test_create_frame_frame_type_normal():
    """ create_frame の frame_type が normal のときのテスト"""
    assert create_frame('normal') == 100


def test_create_frame_frame_type_not_normal():
    """ create_frame の frame_type が normal 以外のときのテスト"""
    assert create_frame('sporty') == 150


def test_create_bumper_bumper_type_normal():
    """ create_bumper の bumper_type が normal のときのテスト"""
    assert create_bumper('normal') == 15


def test_create_bumper_bumper_type_not_normal():
    """ create_bumper の bumper_type が normal 以外のときのテスト"""
    assert create_bumper('sporty') == 20


def test_semifinished_product_interior_is_luxuary_true():
    """
    semifinished_product_interior の is_luxuary が True のときのテスト
    create_handle, create_seat は正常動作するという前提
    """
    handle_type = 'normal'
    seat_type = 'leather'
    is_luxuary = True
    a = create_handle(handle_type)
    b = create_seat(seat_type)
    result = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    assert result == a - b


def test_semifinished_product_interior_is_luxuary_false():
    """
    semifinished_product_interior の is_luxuary が False のときのテスト
    create_handle, create_seat は正常動作するという前提
    """
    handle_type = 'normal'
    seat_type = 'leather'
    is_luxuary = False
    a = create_handle(handle_type)
    b = create_seat(seat_type)
    result = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    assert result == a + b


def test_semifinishued_product_exterior_color_name_red():
    """
    semifinished_product_exterior の color_name が red のときのテスト
    create_frame, create_bumper は正常動作するという前提
    """
    color_name = 'red'
    frame_type = 'normal'
    bumper_type = 'normal'
    c = create_frame(frame_type)
    d = create_bumper(bumper_type)
    result = semifinished_product_exterior(frame_type, bumper_type, color_name)
    assert result == c * d


def test_semifinishued_product_exterior_color_name_not_red():
    """
    semifinished_product_exterior の color_name が red 以外のときのテスト
    create_frame, create_bumper は正常動作するという前提
    """
    color_name = 'blue'
    frame_type = 'normal'
    bumper_type = 'normal'
    c = create_frame(frame_type)
    d = create_bumper(bumper_type)
    result = semifinished_product_exterior(frame_type, bumper_type, color_name)
    assert result == c / d


def test_create_car_is_sporty_true():
    """
    create_car の is_sporty が True のときのテスト
    semifinished_product_interior, semifinished_product_exterior は正常動作するという前提
    """
    handle_type = 'sporty'
    seat_type = 'leather'
    is_luxuary = True
    color_name = 'red'
    frame_type = 'sporty'
    bumper_type = 'sporty'
    is_sporty = True
    interior = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    exterior = semifinished_product_exterior(frame_type, bumper_type, color_name)
    result = create_car(handle_type, seat_type, frame_type, bumper_type, is_luxuary, color_name, is_sporty)
    assert result == f'カッコイイ車です！価格は{interior + exterior}万円！'


def test_create_car_is_sporty_false():
    """
    create_car の is_sporty が False のときのテスト
    semifinished_product_interior, semifinished_product_exterior は正常動作するという前提
    """
    handle_type = 'normal'
    seat_type = 'normal'
    is_luxuary = False
    color_name = 'blue'
    frame_type = 'normal'
    bumper_type = 'normal'
    is_sporty = False
    interior = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    exterior = semifinished_product_exterior(frame_type, bumper_type, color_name)
    result = create_car(handle_type, seat_type, frame_type, bumper_type, is_luxuary, color_name, is_sporty)
    assert result == f'それなりな車です！価格は{interior + exterior}万円！'
