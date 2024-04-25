def is_nonagonal(n):
    """
    Find the nth nonagonal number.

    Args:
        n (int): The position of the nonagonal number to find.

    Returns:
        int: The nth nonagonal number.
    """
    return n * (7 * n - 5) // 2

def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)