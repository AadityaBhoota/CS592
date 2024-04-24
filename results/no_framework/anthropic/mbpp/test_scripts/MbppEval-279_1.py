def is_num_decagonal(n):
    """
    Write a function to find the nth decagonal number.

    Examples:
    is_num_decagonal(3) == 27
    is_num_decagonal(7) == 175
    is_num_decagonal(10) == 370
    """
    return int(n * (3 * n - 2) / 2)

def check(candidate):
    assert is_num_decagonal(3) == 27
    assert is_num_decagonal(7) == 175
    assert is_num_decagonal(10) == 370

check(is_num_decagonal)