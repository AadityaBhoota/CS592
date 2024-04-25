import math

def is_perfect_square(n):
    sqrt_n = math.sqrt(n)
    return sqrt_n.is_integer() and sqrt_n ** 2 == n

def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)