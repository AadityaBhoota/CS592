def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
from math import factorial

def sum_of_product(n):
    sum_product = 0
    for k in range(1, n):
        product = factorial(n) / (factorial(k) * factorial(n - k))
        sum_product += product * factorial(k) * factorial(n - k)
    return sum_product

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)