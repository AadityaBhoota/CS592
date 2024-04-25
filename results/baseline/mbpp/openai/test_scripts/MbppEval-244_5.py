import math

def next_Perfect_Square(N):
    root = int(math.sqrt(N))  # Compute the square root of N and take integer part
    next_square = (root + 1) ** 2  # Calculate the next perfect square by squaring the next integer
    
    return next_square

# Test cases




def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)