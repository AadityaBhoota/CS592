def binomial_Coeff(n, k):
    """
    Calculate the binomial coefficient of n choose k.
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n-k))

def factorial(n):
    """
    Calculate the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_Of_product(n):
    """
    Calculate the sum of the product of consecutive binomial coefficients.
    """
    total = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            total += binomial_Coeff(i, i) * binomial_Coeff(j, j)
    return total

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)