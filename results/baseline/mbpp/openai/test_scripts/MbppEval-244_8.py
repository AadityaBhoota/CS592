import math

def next_Perfect_Square(N):
    sqrt = math.isqrt(N)
    next_square = (sqrt + 1) ** 2
    return next_square

# Test the function with the provided examples




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)