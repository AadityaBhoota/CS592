import math

def is_perfect_square(n):
    square_root = math.sqrt(n)
    if square_root.is_integer():
        return True
    else:
        return False

def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)