import math  
def even_binomial_Coeff_Sum( n): 
    '''
    Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.

    Examples:
    even_binomial_Coeff_Sum(4) == 8
    even_binomial_Coeff_Sum(6) == 32
    even_binomial_Coeff_Sum(2) == 2
    '''
import math

def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def even_binomial_coeff_sum(n):
    total_sum = 0
    for k in range(n + 1):
        if k % 2 == 0:
            total_sum += binomial_coefficient(n, k)
    return total_sum

# Testing the function




def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)