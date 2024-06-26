def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
from math import comb

def sum_of_product(n):
    sum_result = 0
    for i in range(1, n+1):
        sum_result += comb(n,i) * comb(n,i-1)
    return sum_result

# Test cases




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)