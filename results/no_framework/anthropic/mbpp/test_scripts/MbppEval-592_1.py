def binomial_Coeff(n, k):
    """
    Calculates the binomial coefficient (n choose k).
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n-k))

def factorial(n):
    """
    Calculates the factorial of a given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_Of_product(n):
    """
    Calculates the sum of the product of consecutive binomial coefficients.
    """
    total = 0
    for k in range(n+1):
        total += binomial_Coeff(n, k) * binomial_Coeff(n, k+1)
    return total

# Examples




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)