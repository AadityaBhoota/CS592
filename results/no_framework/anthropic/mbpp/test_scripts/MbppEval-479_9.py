def first_Digit(n):
    """
    Finds the first digit of a given number.

    Args:
        n (int): The number to find the first digit of.

    Returns:
        int: The first digit of the given number.
    """
    # Convert the number to a string and return the first character
    return int(str(n)[0])

def check(candidate):
    assert first_Digit(123) == 1
    assert first_Digit(456) == 4
    assert first_Digit(12) == 1

check(first_Digit)