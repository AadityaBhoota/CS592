def is_octagonal(n):
    """
    Computes the nth octagonal number.

    Args:
        n (int): The index of the octagonal number to compute.

    Returns:
        int: The nth octagonal number.
    """
    return n * (3 * n - 2)

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)