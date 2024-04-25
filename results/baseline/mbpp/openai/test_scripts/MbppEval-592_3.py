def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
def binomial_coeff(n, k):
    def factorial(num):
        return 1 if num == 0 else num * factorial(num - 1)

    return factorial(n) // (factorial(k) * factorial(n - k))

def sum_of_product(n):
    result = 0
    for i in range(n+1):
        result += binomial_coeff(n, i) * binomial_coeff(n, i+1)
    return result

# Test the function with some examples




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)