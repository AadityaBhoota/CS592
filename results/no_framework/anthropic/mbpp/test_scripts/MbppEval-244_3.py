import math

def next_Perfect_Square(N):
    """
    Write a python function to find the next perfect square greater than a given number.

    Examples:
    next_Perfect_Square(35) == 36
    next_Perfect_Square(6) == 9
    next_Perfect_Square(9) == 16
    """
    # Calculate the square root of the given number
    sqrt = math.sqrt(N)
    
    # If the square root is an integer, return the next perfect square
    if sqrt.is_integer():
        return int(sqrt + 1) ** 2
    
    # Otherwise, return the next perfect square above the given number
    return int(sqrt) ** 2 + 2 * int(sqrt) + 1

def check(candidate):
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16

check(next_Perfect_Square)