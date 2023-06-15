def create_handle(handle_type):
    """ パーツA handle_type に準じた内装部品ハンドルを供給する """
    if handle_type == 'normal':
        return 10
    else:
        return 20


def create_seat(seat_type):
    """ パーツB seat_type に準じた内装部品座席を供給する """
    if seat_type == 'leather':
        return 50
    else:
        return 30


def create_frame(frame_type):
    """ パーツC frame_type に準じた外装部品車体を供給する """
    if frame_type == 'normal':
        return 100
    else:
        return 150


def create_bumper(bumper_type):
    """ パーツD bumper_type に準じた外装部品バンパーを供給する """
    if bumper_type == 'normal':
        return 15
    else:
        return 20


def semifinished_product_interior(handle_type, seat_type, is_luxuary):
    """ 半製品その1 product_name と type_name から内装を作る。is_luxuary ならば豪華にする """
    a = create_handle(handle_type)
    b = create_seat(seat_type)
    if is_luxuary:
        return a - b
    else:
        return a + b


def semifinished_product_exterior(frame_type, bumper_type, color_name):
    """ 半製品その2 frame, bumper から外装を作り、 color_name で指定された色で塗装する """
    c = create_frame(frame_type)
    d = create_bumper(bumper_type)
    if color_name == 'red':
        return c * d
    else:
        return c / d


def create_car(handle_type, seat_type, frame_type, bumper_type,
               is_luxuary, color_name, is_sporty):
    """ 製品 interior, exterior を組み合わせ製品を作る。is_sporty のときはカッコよくする """
    interior = semifinished_product_interior(handle_type, seat_type, is_luxuary)
    exterior = semifinished_product_exterior(frame_type, bumper_type, color_name)
    if is_sporty:
        return f'カッコイイ車です！価格は{interior + exterior}万円！'
    else:
        return f'それなりな車です！価格は{interior + exterior}万円！'


if __name__ == '__main__':
    result = create_car('normal', 'leather', 'normal', 'normal', False, 'red', False)
    print(result)
