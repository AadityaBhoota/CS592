def centered_hexagonal_number(n):
    """
    Find the nth centered hexagonal number.

    The formula for the nth centered hexagonal number is:
    C(n) = 3n^2 - 3n + 1

    Args:
        n (int): The position of the centered hexagonal number.

    Returns:
        int: The nth centered hexagonal number.
    """
    return 3 * n**2 - 3 * n + 1

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217

check(centered_hexagonal_number)