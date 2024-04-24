import math

def next_Perfect_Square(N):
    # Calculate the square root of the given number
    square_root = math.isqrt(N) + 1
    # Calculate the next perfect square
    next_square = square_root * square_root
    return next_square

# Test the function with the examples




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)