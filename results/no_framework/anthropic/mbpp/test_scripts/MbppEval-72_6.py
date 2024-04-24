import math

def dif_Square(n):
    """
    Checks whether the given number can be represented as the difference of two squares.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number can be represented as the difference of two squares, False otherwise.
    """
    # Check if the number is negative or zero
    if n <= 0:
        return False

    # Check if the number is a perfect square
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n:
        return True

    # Check if the number can be represented as the difference of two squares
    for i in range(1, sqrt + 1):
        j = n - i * i
        if j > 0 and int(math.sqrt(j)) * int(math.sqrt(j)) == j:
            return True

    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)