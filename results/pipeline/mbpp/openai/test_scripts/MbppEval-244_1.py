import math

def next_Perfect_Square(N):
    square_root = math.sqrt(N)
    next_square = math.ceil(square_root)
    next_perfect_square = next_square ** 2
    return next_perfect_square

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)