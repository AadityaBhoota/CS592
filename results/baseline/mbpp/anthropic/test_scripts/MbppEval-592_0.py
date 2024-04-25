def binomial_Coeff(n, k):
    """
    Calculates the binomial coefficient (n choose k).
    """
    if k == 0 or k == n:
        return 1
    else:
        return binomial_Coeff(n-1, k-1) + binomial_Coeff(n-1, k)

def sum_Of_product(n):
    """
    Calculates the sum of the product of consecutive binomial coefficients.
    """
    total = 0
    for k in range(n+1):
        total += binomial_Coeff(n, k) * binomial_Coeff(n, k+1)
    return total

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)