def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
def sum_of_product(n):
    def calculate_binomial_coeff(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return calculate_binomial_coeff(n-1, k-1) + calculate_binomial_coeff(n-1, k)

    if n == 0:
        return 0

    total_sum = 0
    for i in range(n):
        total_sum += calculate_binomial_coeff(n-1, i) * calculate_binomial_coeff(n-1, i+1)

    return total_sum

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)