import math

def is_perfect_square(n):
    """
    Checks whether the given number is a perfect square or not.
    
    Args:
    n (int): The number to be checked.
    
    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        # Calculate the square root of the number
        sqrt = math.sqrt(n)
        
        # Check if the square root is an integer
        return sqrt.is_integer()

def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)