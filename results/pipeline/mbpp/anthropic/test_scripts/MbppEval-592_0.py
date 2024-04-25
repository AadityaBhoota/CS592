def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
def sum_Of_product(n):
    total = 0
    for k in range(n+1):
        total += factorial(n) / (factorial(k) * factorial(n-k))
    return total

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)