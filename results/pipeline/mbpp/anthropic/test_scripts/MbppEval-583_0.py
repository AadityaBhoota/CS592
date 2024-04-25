import math

def catalan_number(num):
    """
    Write a function which returns nth catalan number.

    Examples:
    catalan_number(10) == 16796
    catalan_number(9) == 4862
    catalan_number(7) == 429
    """
    if num < 0:
        raise ValueError("Input must be a non-negative integer")

    # Calculate the binomial coefficient (2*n)! / (n! * n!)
    numerator = math.factorial(2 * num)
    denominator = math.factorial(num) * math.factorial(num)
    binomial_coeff = numerator // denominator

    # Calculate the nth Catalan number
    catalan_num = binomial_coeff // (num + 1)
    return catalan_num

def check(candidate):
    assert catalan_number(10)==16796
    assert catalan_number(9)==4862
    assert catalan_number(7)==429

check(catalan_number)