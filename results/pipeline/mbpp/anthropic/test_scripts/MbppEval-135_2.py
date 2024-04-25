def hexagonal_num(n):
    """
    Write a function to find the nth hexagonal number.

    Examples:
    hexagonal_num(10) == 190
    hexagonal_num(5) == 45
    hexagonal_num(7) == 91
    """
    return n * (2 * n - 1)

def check(candidate):
    assert hexagonal_num(10) == 190
    assert hexagonal_num(5) == 45
    assert hexagonal_num(7) == 91

check(hexagonal_num)