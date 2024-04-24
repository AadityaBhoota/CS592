import math

def is_perfect_square(n):
    """
    Check whether the given number is a perfect square or not.
    
    Args:
        n (int): The number to be checked.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    
    square_root = int(math.sqrt(n))
    return square_root * square_root == n

def check(candidate):
    assert not is_perfect_square(10)
    assert is_perfect_square(36)
    assert not is_perfect_square(14)
    assert is_perfect_square(14*14)
    assert not is_perfect_square(125)
    assert is_perfect_square(125*125)

check(is_perfect_square)