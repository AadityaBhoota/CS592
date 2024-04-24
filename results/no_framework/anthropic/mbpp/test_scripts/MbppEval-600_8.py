def is_Even(n):
    """
    Checks whether the given number is even or not.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False

check(is_Even)