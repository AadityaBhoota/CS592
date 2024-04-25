import math

def dif_Square(n):
    """
    Check whether the given number can be represented as the difference of two squares.
    
    Args:
        n (int): The number to be checked.
    
    Returns:
        bool: True if n can be represented as the difference of two squares, False otherwise.
    """
    sqrt_n = int(math.sqrt(n))
    for x in range(sqrt_n + 1):
        if n == x**2 - (x+1)**2:
            return True
    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)