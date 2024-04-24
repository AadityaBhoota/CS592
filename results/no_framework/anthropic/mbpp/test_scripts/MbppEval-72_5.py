import math

def dif_Square(n):
    """
    Check whether the given number can be represented as the difference of two squares or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as the difference of two squares, False otherwise.
    """
    # Check if the number is a perfect square
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n:
        return True

    # Check if the number can be represented as the difference of two squares
    for i in range(1, sqrt + 1):
        j = i + 1
        while i * i + j * j <= n:
            if i * i + j * j == n:
                return True
            j += 1

    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)