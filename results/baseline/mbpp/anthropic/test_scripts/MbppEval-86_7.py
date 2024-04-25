def centered_hexagonal_number(n):
    """
    Write a function to find nth centered hexagonal number.

    Examples:
    centered_hexagonal_number(10) == 271
    centered_hexagonal_number(2) == 7
    centered_hexagonal_number(9) == 217
    """
    return n * (2 * n - 1)

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217

check(centered_hexagonal_number)