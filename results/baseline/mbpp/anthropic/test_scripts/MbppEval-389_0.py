def find_lucas(n):
    """
    Write a function to find the n'th lucas number.

    Examples:
    find_lucas(9) == 76
    find_lucas(4) == 7
    find_lucas(3) == 4
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)

def check(candidate):
    assert find_lucas(9) == 76
    assert find_lucas(4) == 7
    assert find_lucas(3) == 4

check(find_lucas)