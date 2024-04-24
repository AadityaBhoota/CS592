import math

def even_binomial_Coeff_Sum(n):
    """
    Calculates the sum of even index binomial coefficients for a given positive integer n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of even index binomial coefficients.
    """
    total_sum = 0
    for i in range(0, n+1, 2):
        total_sum += math.comb(n, i)
    return total_sum

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)