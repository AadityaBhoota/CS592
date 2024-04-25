import math

def is_woodall(x):
    """
    Check if the given number is a Woodall number.

    Args:
        x (int): The number to be checked.

    Returns:
        bool: True if x is a Woodall number, False otherwise.
    """
    n = math.log2(x + 1) - 1
    return x == 2 ** int(n) + int(n) - 1

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)