import math

def next_Perfect_Square(N):
    """
    Write a python function to find the next perfect square greater than a given number.

    Examples:
    next_Perfect_Square(35) == 36
    next_Perfect_Square(6) == 9
    next_Perfect_Square(9) == 16
    """
    sqrt = math.sqrt(N)
    next_sqrt = math.ceil(sqrt)
    next_perfect_square = next_sqrt ** 2
    return int(next_perfect_square)

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)