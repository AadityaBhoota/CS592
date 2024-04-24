import math

def next_Perfect_Square(N):
    perfect_square = math.isqrt(N)**2
    next_perfect_square = (math.isqrt(N) + 1)**2
    return next_perfect_square

# Test cases




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)