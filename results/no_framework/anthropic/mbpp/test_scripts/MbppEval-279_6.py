def is_num_decagonal(n):
    """
    Finds the nth decagonal number.

    Args:
        n (int): The position of the decagonal number to be found.

    Returns:
        int: The nth decagonal number.
    """
    return n * (3 * n - 2)

def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370

check(is_num_decagonal)