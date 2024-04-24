def geometric_sum(n):
    """
    Calculate the geometric sum of n-1.
    
    Args:
        n (int): The number of terms in the geometric sum.
        
    Returns:
        float: The geometric sum of n-1.
    """
    if n == 0:
        return 0
    else:
        return 1 / (2 ** (n - 1)) + geometric_sum(n - 1)

def check(candidate):
    assert geometric_sum(7) == 1.9921875
    assert geometric_sum(4) == 1.9375
    assert geometric_sum(8) == 1.99609375

check(geometric_sum)