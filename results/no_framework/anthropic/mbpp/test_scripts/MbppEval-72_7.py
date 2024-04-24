import math

def dif_Square(n):
    """
    Check whether the given number can be represented as the difference of two squares or not.

    Examples:
    dif_Square(5) == True
    dif_Square(10) == False
    dif_Square(15) == True
    """
    # Check if the number is a perfect square
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n:
        return True

    # Check if the number can be expressed as the difference of two squares
    for i in range(1, sqrt + 1):
        j = int(math.sqrt(n + i * i))
        if j * j == n + i * i:
            return True

    return False

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True

check(dif_Square)