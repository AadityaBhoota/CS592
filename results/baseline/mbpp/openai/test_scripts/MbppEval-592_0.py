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
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    return factorial(n) / (factorial(k) * factorial(n - k))

def sum_of_product(n):
    total_sum = 0
    for i in range(1, n):
        total_sum += binomial_coeff(n, i) * binomial_coeff(n, i + 1)
    return total_sum

# Examples




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)