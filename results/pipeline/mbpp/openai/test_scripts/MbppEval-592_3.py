def binomial_Coeff(n,k): 
    '''
    Write a python function to find the sum of the product of consecutive binomial co-efficients.

    Examples:
    sum_Of_product(3) == 15
    sum_Of_product(4) == 56
    sum_Of_product(1) == 1
    '''
def binomial_coeff(n, k):
    if k == 0 or k == n:
        return 1
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res

def sum_of_product(n):
    total_sum = 0
    if n < 2:
        return n
    for k in range(n - 1):
        total_sum += binomial_coeff(n, k) + binomial_coeff(n, k + 1)
    return total_sum

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)