def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
def sum_of_product(n):
    def binomial_coeff(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coeff(n - 1, k - 1) + binomial_coeff(n - 1, k)

    result = 0
    for i in range(1, n+1):
        result += binomial_coeff(n, i) * binomial_coeff(n, i-1)
    
    return result

# Test cases




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)