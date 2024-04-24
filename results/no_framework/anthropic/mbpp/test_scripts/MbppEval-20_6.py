def is_woodall(x):
    """
    Checks if the given number is a Woodall number.

    A Woodall number is a number of the form 2^n - n - 1, where n is a positive integer.

    Args:
        x (int): The number to check.

    Returns:
        bool: True if the number is a Woodall number, False otherwise.
    """
    n = 0
    while True:
        woodall = 2 ** n - n - 1
        if woodall == x:
            return True
        elif woodall > x:
            return False
        n += 1

def check(candidate):
    assert is_woodall(383) == True
    assert is_woodall(254) == False
    assert is_woodall(200) == False

check(is_woodall)