def centered_hexagonal_number(n):
    """
    Finds the nth centered hexagonal number.

    Args:
        n (int): The position of the centered hexagonal number to find.

    Returns:
        int: The nth centered hexagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    return n * (5 * n - 4)

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217

check(centered_hexagonal_number)