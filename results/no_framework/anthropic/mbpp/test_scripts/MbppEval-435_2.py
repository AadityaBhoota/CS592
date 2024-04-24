def last_Digit(n):
    """
    Find the last digit of a given number.

    Args:
        n (int): The number to find the last digit of.

    Returns:
        int: The last digit of the given number.
    """
    return n % 10

def check(candidate):
    assert last_Digit(123) == 3
    assert last_Digit(25) == 5
    assert last_Digit(30) == 0

check(last_Digit)