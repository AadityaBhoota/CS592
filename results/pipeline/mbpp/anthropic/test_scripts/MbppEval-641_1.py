def is_nonagonal(n): 
    '''
    Write a function to find the nth nonagonal number.

    Examples:
    is_nonagonal(10) == 325
    is_nonagonal(15) == 750
    is_nonagonal(18) == 1089
    '''
def get_nth_nonagonal(n):
    """
    Calculate the nth nonagonal number.

    Args:
        n (int): A positive integer representing the index of the nonagonal number.

    Returns:
        int: The nth nonagonal number.

    Raises:
        ValueError: If `n` is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return n * (7 * n - 5) // 2

def check(candidate):
    assert is_nonagonal(10) == 325
    assert is_nonagonal(15) == 750
    assert is_nonagonal(18) == 1089

check(is_nonagonal)