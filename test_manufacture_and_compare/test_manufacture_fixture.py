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


@pytest.fixture
def setup_interior():
    print('\nsetup')
    handle_type = 'normal'
    seat_type = 'leather'
    a = create_handle(handle_type)
    b = create_seat(seat_type)
    yield handle_type, seat_type, a, b
    print('\nteardown')


def test_semifinished_product_interior_is_luxuary_true(setup_interior):
    """
    semifinished_product_interior の is_luxuary が True のときのテスト
    create_handle, create_seat は正常動作するという前提
    """

    is_luxuary = True
    handle_type, seat_type, a, b = setup_interior
    result = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    assert result == a - b


def test_semifinished_product_interior_is_luxuary_false(setup_interior):
    """
    semifinished_product_interior の is_luxuary が False のときのテスト
    create_handle, create_seat は正常動作するという前提
    """
    is_luxuary = False
    handle_type, seat_type, a, b = setup_interior
    result = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    assert result == a + b


@pytest.fixture
def setup_exterior():
    print('\nsetup')
    frame_type = 'normal'
    bumper_type = 'normal'
    c = create_frame(frame_type)
    d = create_bumper(bumper_type)
    yield frame_type, bumper_type, c, d
    print('\nteardown')


def test_semifinishued_product_exterior_color_name_red(setup_exterior):
    """
    semifinished_product_exterior の color_name が red のときのテスト
    create_frame, create_bumper は正常動作するという前提
    """
    color_name = 'red'
    frame_type, bumper_type, c, d = setup_exterior
    result = semifinished_product_exterior(frame_type, bumper_type, color_name)
    assert result == c * d


def test_semifinishued_product_exterior_color_name_not_red(setup_exterior):
    """
    semifinished_product_exterior の color_name が red 以外のときのテスト
    create_frame, create_bumper は正常動作するという前提
    """
    color_name = 'blue'
    frame_type, bumper_type, c, d = setup_exterior
    result = semifinished_product_exterior(frame_type, bumper_type, color_name)
    assert result == c / d


@pytest.fixture
def setup_car():
    print('\nsetup')
    handle_type = 'normal'
    seat_type = 'normal'
    color_name = 'blue'
    frame_type = 'normal'
    bumper_type = 'normal'
    is_luxuary = True
    a = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    b = semifinished_product_exterior(frame_type, bumper_type, color_name)
    interior = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    exterior = semifinished_product_exterior(frame_type, bumper_type, color_name)
    result_dict = {
        'handle_type': handle_type,
        'seat_type': seat_type,
        'frame_type': frame_type,
        'bumper_type': bumper_type,
        'color_name': color_name,
        'a': a,
        'b': b,
        'is_luxuary': is_luxuary,
        'interior': interior,
        'exterior': exterior
    }
    yield result_dict
    print('\nteardown')


def test_create_car_is_sporty_true(setup_car):
    """
    create_car の is_sporty が True のときのテスト
    semifinished_product_interior, semifinished_product_exterior は正常動作するという前提
    """
    is_sporty = True
    result_dict = setup_car

    result = create_car(result_dict['handle_type'], result_dict['seat_type'], result_dict['frame_type'],
                        result_dict['bumper_type'], result_dict['is_luxuary'], result_dict['color_name'], is_sporty)
    assert result == f'カッコイイ車です！価格は{result_dict["interior"] + result_dict["exterior"]}万円！'


def test_create_car_is_sporty_false(setup_car):
    """
    create_car の is_sporty が False のときのテスト
    semifinished_product_interior, semifinished_product_exterior は正常動作するという前提
    """

    is_sporty = False
    result_dict = setup_car

    result = create_car(result_dict['handle_type'], result_dict['seat_type'], result_dict['frame_type'],
                        result_dict['bumper_type'], result_dict['is_luxuary'], result_dict['color_name'], is_sporty)
    assert result == f'それなりな車です！価格は{result_dict["interior"] + result_dict["exterior"]}万円！'
