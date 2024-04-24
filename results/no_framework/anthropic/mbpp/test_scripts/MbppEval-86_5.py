def centered_hexagonal_number(n):
    """
    Write a function to find the nth centered hexagonal number.

    The formula for the nth centered hexagonal number is:
    n * (5 * n - 4)

    Examples:
    centered_hexagonal_number(10) == 271
    centered_hexagonal_number(2) == 7
    centered_hexagonal_number(9) == 217
    """
    return n * (5 * n - 4)

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217

check(centered_hexagonal_number)