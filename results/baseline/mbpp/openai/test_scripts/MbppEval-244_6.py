import math

def next_Perfect_Square(N):
    square_root = math.ceil(math.sqrt(N))
    return square_root ** 2

# Test the function




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)