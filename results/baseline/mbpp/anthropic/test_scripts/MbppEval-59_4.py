def is_octagonal(n):
    """
    Find the nth octagonal number.

    Args:
        n (int): The position of the octagonal number to find.

    Returns:
        int: The nth octagonal number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    return n * (3 * n - 2)

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)