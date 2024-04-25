from math import gamma

def catalan_number(num):
    """
    Returns the nth Catalan number.
    """
    numerator = gamma(2 * num + 1)
    denominator = gamma(num + 1) * gamma(num + 1)
    return int(numerator / denominator)

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)