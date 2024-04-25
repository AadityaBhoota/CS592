import math

def next_Perfect_Square(N):
    square_root = math.sqrt(N)
    if square_root.is_integer():
        next_square = (int(square_root) + 1) ** 2
    else:
        next_square = math.ceil(square_root) ** 2

    return next_square

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)