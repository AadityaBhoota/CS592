import math

def even_binomial_Coeff_Sum(n):
    '''
    Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.

    Examples:
    even_binomial_Coeff_Sum(4) == 8
    even_binomial_Coeff_Sum(6) == 32
    even_binomial_Coeff_Sum(2) == 2
    '''
    total = 0
    for i in range(0, n+1, 2):
        total += math.comb(n, i)
    return total

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)