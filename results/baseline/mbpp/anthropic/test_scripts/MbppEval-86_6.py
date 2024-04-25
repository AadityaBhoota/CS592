def centered_hexagonal_number(n):
    """
    Finds the nth centered hexagonal number.

    The centered hexagonal number is a figurate number that
    represents a hexagon with a dot in the center and all
    other dots surrounding the center dot in a hexagonal
    shape.

    The formula to calculate the nth centered hexagonal number is:
    C_h(n) = 3n^2 - 3n + 1

    Args:
        n (int): The position of the centered hexagonal number to find.

    Returns:
        int: The nth centered hexagonal number.
    """
    return 3 * n**2 - 3 * n + 1

def check(candidate):
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(9) == 217

check(centered_hexagonal_number)