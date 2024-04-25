def is_octagonal(n):
    """
    Write a function to find the nth octagonal number.

    Examples:
    is_octagonal(5) == 65
    is_octagonal(10) == 280
    is_octagonal(15) == 645
    """
    return n * (3 * n - 2)

def check(candidate):
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

check(is_octagonal)