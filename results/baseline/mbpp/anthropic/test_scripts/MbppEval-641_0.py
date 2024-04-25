def is_nonagonal(n):
    """
    Write a function to find the nth nonagonal number.

    Examples:
    is_nonagonal(10) == 325
    is_nonagonal(15) == 750
    is_nonagonal(18) == 1089
    """
    return n * (7 * n - 5) // 2

def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)