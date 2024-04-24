import math

def next_Perfect_Square(N):
    # Find the square root of N
    sqrt_N = math.sqrt(N)
    
    # Round up to the nearest integer
    ceil_sqrt_N = math.ceil(sqrt_N)
    
    # Find the next perfect square
    next_square = ceil_sqrt_N ** 2
    
    return next_square

# Test cases




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)