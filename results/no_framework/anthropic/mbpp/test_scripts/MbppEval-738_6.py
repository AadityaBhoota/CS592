def geometric_sum(n):
    """
    Write a function to calculate the geometric sum of n-1.
    Examples:
    geometric_sum(7) == 1.9921875
    geometric_sum(4) == 1.9375
    geometric_sum(8) == 1.99609375
    """
    if n == 0:
        return 0
    else:
        return 1 / (2 ** (n-1)) + geometric_sum(n-1)

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)